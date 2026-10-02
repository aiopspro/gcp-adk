# 📟 ADK-Style Custom OpenAI City Time Checker Agent

A production-grade, decoupled AI Agent framework designed to replicate the clean, object-oriented instantiation pattern of Google's Agent Development Kit (ADK) using the official **OpenAI Python SDK** and the **o3-mini** high-reasoning engine. 

This agent functions as a specialized **City Time Assistant** capable of executing a local Python tool to accurately look up and convert active live times for major cities across the globe without network delays or unstable API dependencies.

---

## 🏗️ Architecture Design & File Structure

During development, forcing dual-mode conversational systems (CLI + Web UI) inside a single executable file introduced runtime pipeline deadlocks. Because Streamlit continually re-evaluates files from top-to-bottom on every user interaction, global execution frames collided with the terminal's infinite blocking `input()` reader loop, freezing the server completely.

### The Decoupled Engineering Blueprint
To solve this, the core system logic is split into a modular two-file pattern:

┌──────────────────────────────────────┐
│         .env CONFIGURATION           │
│   (Authenticated OPENAI_API_KEY)     │
└──────────────────┬───────────────────┘
▼
┌──────────────────────────────────────┐
│              agent.py                │
│  - Custom OpenAIAgent Wrapper Class  │
│  - Static JSON-to-Schema Introspector│
│  - Offline Timezone Tool & CLI Loop  │
└──────────────────┬───────────────────┘
│
▼
┌──────────────────────────────────────┐
│               app.py                 │
│     (Streamlit Web GUI Launcher)     │
└──────────────────────────────────────┘

1. **`agent.py` (Core Engine & CLI Handler):** Houses the `OpenAIAgent` wrapper class which handles dynamic string reflection (`inspect.signature`) to build raw JSON execution tool schemas on system boot without manual declaration blocks. It also contains the safe, non-blocking entrypoint for terminal interactions.
2. **`app.py` (Streamlit GUI Launcher):** Implements an isolated frontend event loop that encapsulates state storage (`st.session_state`) for conversation streaming while visually logging background multi-pass tool invocations.

---

## 🛠️ Installation & Virtual Environment Setup

Follow these steps to deploy and lock dependencies within an isolated virtual environment (`.venv`) on macOS:

```bash
# 1. Create a clean virtual environment space
python3 -m venv .venv

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Upgrade pip package manager
pip install --upgrade pip

# 4. Install all dependencies 
pip install -r requirements.txt
```

### Required `requirements.txt` Payload
Ensure your `requirements.txt` file contains the following libraries:
```text
openai>=1.0.0
streamlit>=1.30.0
python-dotenv>=1.0.0
tzdata>=2023.3
```

---

## ⚙️ Environment Variables Configuration

Before running the application, create a secure file named exactly `.env` in the root project folder containing your validated OpenAI developer keys:

```env
OPENAI_API_KEY=sk-proj-yourActualOpenDataAccessKeyHere...
```

---

## 📟 Usage & Operational Playbooks

This project supports dual interface operations seamlessly out of the same backend modules directory.

### Mode 1: Run the Interactive Terminal CLI
To launch the agent directly into your shell command prompt window, run:
```bash
python3 agent.py
```

### Mode 2: Run the Web Browser Interface (GUI)
To execute the visual web interface dashboard without encountering frozen loading screens, invoke Streamlit in headless server mode:
```bash
streamlit run app.py --server.headless true
```
Upon execution, your default system browser will instantly route to:
👉 **`http://localhost:8501`**

---

## 🔍 Structural Grounding & Tool Capabilities

The agent is fully grounded using a robust, offline Python system function:

### Offline Timezone Mapping (`get_current_time`)
* **Logic:** Operates completely offline without hitting unstable public API network boundaries. Maps city query intents against internal structural dictionaries utilizing the `zoneinfo` database records located right on your Mac storage disk.
* **Supported Core Targets:** Delhi, Mumbai, Berlin, London, Tokyo, New York, Los Angeles.

#### Example UI Execution Prompt Stream
```text
User: what is the current time in delhi right now?

-> Status Spinner: 🛠️ Agent invoking tool: `get_current_time` with args: {'city': 'Delhi'}
-> Status Code: Success. Local timezone database read cleanly.

Agent: The current time in Delhi is 01:37:12 PM.
```