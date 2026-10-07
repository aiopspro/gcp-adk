# ADK Agent Config Framework & CLI Operations

This guide provides the official setup, configuration templates, and runtime instructions for building no-code/low-code workflows using the **Google Agent Development Kit (ADK) Agent Config** feature. 

Agent Config allows you to assemble, scale, and run modular conversational AI agents entirely from declarative YAML configuration text files.

---

## 🛠️ Environment Verification & Setup

Before developing configuration-based workflows, ensure your local system environment is running the required packages. *Note: Python is currently required to execute the Agent Config engine.*

```bash
# 1. Activate your isolated virtual environment space (Mac/Linux example)
source .venv/bin/activate

# 2. Verify that ADK is installed and accessible via your path shell
adk --version
```

---

## 🏗️ Building an Agent Project

Use the ADK scaffolding utility to generate a project folder pre-configured for declarative orchestration schemas.

### 1. Generate the Project Boilerplate
Run the following initialization command in your active terminal window:
```bash
adk create --type=config my_agent
```
This generates a standalone `my_agent/` directory containing two vital baseline target structures:
* `root_agent.yaml` — The structural agent configuration text definition.
* `.env` — Secure environment credentials space.

### 2. Configure Environment Credentials
Open `my_agent/.env` and supply your authorization parameters depending on your deployment pattern:

#### Option A: Direct Gemini API via Google AI Studio
```env
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=<your-Google-Gemini-API-key>
```

#### Option B: Enterprise Vertex AI Access via Google Cloud
```env
GOOGLE_GENAI_USE_ENTERPRISE=1
GOOGLE_CLOUD_PROJECT=<your_gcp_project>
GOOGLE_CLOUD_LOCATION=us-central1
```

### 3. Declarative Blueprint (`my_agent/root_agent.yaml`)
Open the generated YAML file and map your agent's persona. The configuration uses JSON schema validation flags for IDE autocompletion safety:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: assistant_agent
model: gemini-flash-latest
description: A helper agent that can answer users' questions.
instruction: You are an agent to help answer users' various questions.
```

---

## 📟 Agent Runtime Operational Playbook

Navigate directly into the directory containing your configuration file to deploy or interface with your agent:
```bash
cd my_agent
```

You can start your Agent Config-defined system using three distinct runtime strategies:
* `adk web` — Launches an interactive web browser user interface graphical tool dashboard.
* `adk run` — Boots the agent directly within your terminal shell via an interactive CLI.
* `adk api_server` — Hosts the workflow model as a network microservice accessible by other external software systems.

---

## 🔍 Advanced CLI Session Control Matrix

When interacting with your agent using `adk run`, you can pass precise flags to control conversation sessions, historical tracking, and system debugging loops.

### 1. Standard Interactive Execution
```bash
adk run my_agent
```
*Expected terminal message execution flow:*
```text
Running agent my_agent, type exit to exit.
[user]: What's the weather in New York?
[my_agent]: The weather in New York is sunny with a temperature of 25°C.
[user]: exit
```

### 2. Session Persistence and Recovery (*Python Only*)

#### Save On-Close Sessions
To force the framework to output a JSON compilation of your chat logs when you issue an exit keyword command, specify a destination path:
```bash
adk run --save_session path/to/my_agent
```
*Alternatively, you can assign a custom unique session name from the start:*
```bash
adk run --save_session --session_id my_session path/to/my_agent
```

#### Resume Existing Saved Sessions
To pick up a previous chat thread, load its state variables and events map back into memory by executing:
```bash
adk run --resume path/to/my_agent/my_session.session.json path/to/my_agent
```

#### Non-Interactive Replay Automation
For CI/CD testing pipelines or script checks, you can feed a static input JSON file containing mock user steps straight to your agent without an active shell prompt:
```bash
adk run --replay path/to/input.json path/to/my_agent
```
*The expected mock structure payload (`input.json`) must look like this:*
```json
{
  "state": {"key": "value"},
  "queries": ["What is 2 + 2?", "What is the capital of France?"]
}
```
