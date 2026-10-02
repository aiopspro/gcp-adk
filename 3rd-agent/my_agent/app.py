import streamlit as st
from agent import OpenAIAgent, get_current_time, analyze_local_cost_logs

# Streamlit App Configurations
st.set_page_config(page_title="FinOps Agent Web UI", page_icon="📈")
st.title("📈 o3-mini FinOps AI Agent Dashboard")
st.caption("Analyzing local infrastructure log directories natively")

# Cache the agent layout instance so it holds state across widget adjustments
@st.cache_resource
def load_gui_agent():
    return OpenAIAgent(
        model='o3-mini', name='root_agent', execution_mode="gui",
        instruction="You are a specialized FinOps Architect. Use your tools to check time or inspect and summarize local cost export log files.",
        tools=[get_current_time, analyze_local_cost_logs]
    )

gui_agent = load_gui_agent()

# Establish conversation runtime containers
if "gui_messages" not in st.session_state:
    st.session_state.gui_messages = [{"role": "system", "content": gui_agent.instruction}]
if "display_history" not in st.session_state:
    st.session_state.display_history = []

# Display running chat log parameters
for msg in st.session_state.display_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Chat Prompt Interceptor
if user_query := st.chat_input("Ask me to analyze gcp_cost_export.log..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.display_history.append({"role": "user", "content": user_query})
    
    with st.chat_message("assistant"):
        with st.spinner("o3-mini processing cost calculations..."):
            resp = gui_agent.run(user_query, st.session_state.gui_messages)
            st.markdown(resp)
    st.session_state.display_history.append({"role": "assistant", "content": resp})
