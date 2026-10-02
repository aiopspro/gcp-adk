import os
import sys
import json
import inspect
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    print("\n❌ CRITICAL ERROR: OpenAI API Key not found!")
    sys.exit(1)

class OpenAIAgent:
    def __init__(self, model: str, name: str, instruction: str, tools: list, execution_mode: str = "cli"):
        self.client = OpenAI()
        self.model = model
        self.name = name
        self.instruction = instruction
        self.execution_mode = execution_mode
        self.runnable_tools = {func.__name__: func for func in tools}
        self.tools_schema = self._autogenerate_schemas(tools)

    def _autogenerate_schemas(self, tools: list) -> list:
        schemas = []
        for func in tools:
            doc = inspect.getdoc(func) or f"Execute function {func.__name__}"
            sig = inspect.signature(func)
            properties = {}
            required_params = []
            for param_name, param in sig.parameters.items():
                param_type = "string"
                if param.annotation == int: param_type = "integer"
                elif param.annotation == dict: param_type = "object"
                properties[param_name] = {"type": param_type, "description": f"The {param_name} parameter value."}
                if param.default == inspect.Parameter.empty: required_params.append(param_name)
            schemas.append({
                "type": "function",
                "function": {
                    "name": func.__name__,
                    "description": doc,
                    "parameters": {"type": "object", "properties": properties, "required": required_params}
                }
            })
        return schemas

    def run(self, user_prompt: str, stream_messages: list) -> str:
        stream_messages.append({"role": "user", "content": user_prompt})
        response = self.client.chat.completions.create(
            model=self.model, messages=stream_messages, tools=self.tools_schema, tool_choice="auto"
        )
        response_message = response.choices[0].message
        
        if response_message.tool_calls:
            stream_messages.append(response_message)
            for tool_call in response_message.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments)
                
                if self.execution_mode == "gui":
                    import streamlit as st
                    with st.status(f"🛠️ Agent invoking tool: `{func_name}`...", expanded=True) as status:
                        st.write(f"**Arguments:** {func_args}")
                        executable = self.runnable_tools[func_name]
                        execution_result = executable(**func_args)
                        st.write(f"**Result:** {execution_result}")
                        status.update(label="Tool executed successfully!", state="complete")
                else:
                    print(f"-> [ADK Tool execution]: '{func_name}' with parameters: {func_args}")
                    executable = self.runnable_tools[func_name]
                    execution_result = executable(**func_args)
                
                stream_messages.append({
                    "tool_call_id": tool_call.id, "role": "tool", "name": func_name, "content": json.dumps(execution_result)
                })
            
            second_response = self.client.chat.completions.create(model=self.model, messages=stream_messages)
            final_text = second_response.choices[0].message.content
        else:
            final_text = response_message.content
            
        stream_messages.append({"role": "assistant", "content": final_text})
        return final_text

def get_current_time(city: str) -> dict:
    """Returns the current live time in a specified city using a local timezone database."""
    city_lower = city.lower().strip()
    tz_mapping = {
        "delhi": "Asia/Kolkata", "mumbai": "Asia/Kolkata", "india": "Asia/Kolkata",
        "germany": "Europe/Berlin", "berlin": "Europe/Berlin", "london": "Europe/London",
        "uk": "Europe/London", "tokyo": "Asia/Tokyo", "japan": "Asia/Tokyo",
        "new york": "America/New_York", "los angeles": "America/Los_Angeles"
    }
    target_tz_str = tz_mapping.get(city_lower)
    if not target_tz_str:
        return {"status": "fallback", "time": datetime.now().strftime("%I:%M:%S %p")}
    return {"status": "success", "city": city, "time": datetime.now(ZoneInfo(target_tz_str)).strftime("%I:%M:%S %p")}

# RUN TERMINAL CLI MODE DIRECTLY
if __name__ == "__main__":
    cli_agent = OpenAIAgent(
        model='o3-mini', name='root_agent', execution_mode="cli",
        instruction="You are a helpful assistant that tells the time. Use 'get_current_time' tool.",
        tools=[get_current_time]
    )
    print("="*60)
    print(f"📟 Terminal CLI Active: {cli_agent.name}")
    print("Type 'exit' or 'quit' to kill this session.")
    print("="*60)
    cli_messages = [{"role": "system", "content": cli_agent.instruction}]
    while True:
        try:
            query = input("\nYou: ").strip()
            if not query or query.lower() in ['exit', 'quit']: break
            print("Thinking... (o3-mini active)")
            output = cli_agent.run(query, cli_messages)
            print(f"\nAgent:\n{output}")
        except KeyboardInterrupt:
            break
