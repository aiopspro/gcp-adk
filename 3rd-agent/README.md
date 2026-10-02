# 📈 ADK-Style Custom OpenAI FinOps AI Agent Dashboard

A production-grade, decoupled AI Agent framework designed to replicate the clean, object-oriented instantiation pattern of Google's Agent Development Kit (ADK) using the official **OpenAI Python SDK** and the **o3-mini** high-reasoning engine.

This agent functions as an automated **FinOps AI Architect** capable of executing local Python system toolsets natively—such as offline global timezone tracking and local file-system infrastructure log analytics—without breaking environment pipelines.

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
│  - System Tools & Terminal CLI Loop  │
└──────────────────┬───────────────────┘
│
▼
┌──────────────────────────────────────┐
│               app.py                 │
│     (Streamlit Web GUI Launcher)     │
└──────────────────────────────────────┘

1. **`agent.py` (Core Engine & CLI Handler):** Houses the `OpenAIAgent` wrapper class which handles dynamic string reflection (`inspect.signature`) to build raw JSON execution function schemas on system boot without manual declaration blocks. It also contains the safe, non-blocking execution entrypoint for terminal interactions.
2. **`app.py` (Streamlit GUI Launcher):** Implements an isolated frontend event loop that encapsulates state storage (`st.session_state`) for conversation streaming while visually logging background multi-pass tool encounters.

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

# 4. Install all decoupled dependencies 
pip install -r requirements.txt
```

### Required `requirements.txt` Payload
Ensure your `requirements.txt` file contains the following libraries:
```text
openai>=1.0.0
streamlit>=1.30.0
python-dotenv>=1.0.0
beautifulsoup4>=4.12.0
requests>=2.31.0
tzdata>=2023.3
```

---

## ⚙️ Environment Variables Configuration

Before running any tasks, create a secure file named exactly `.env` in the root project folder containing your validated OpenAI developer keys:

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

### Mode 2: Run the High-Fidelity Web Browser Interface (GUI)
To execute the visual web interface dashboard without encountering frozen onboarding screens, invoke Streamlit in headless server mode:
```bash
streamlit run app.py --server.headless true
```
Upon execution, your default system browser will instantly route to:
👉 **`http://localhost:8501`**

---

## 🔍 Structural Grounding & Tool Capabilities

The agent is decoupled and fully grounded using two native Python system functions:

### 1. Offline Timezone Mapping (`get_current_time`)
* **Logic:** Operates completely offline without hitting unstable public API network boundaries. Maps city query intents against internal structural dictionaries utilizing `zoneinfo` database records located right on your Mac storage disk.

### 2. Local File System Log Cost Analyzer (`analyze_local_cost_logs`)
* **Logic:** Dynamically reads structural text/log exports straight out of your machine directory logs using path-traversal sanitation guidelines (`os.path.basename`) for advanced cost engineering profiling checks.

#### Sample Input Dataset Log Target (`gcp_cost_export.log`)
Place a text log in your root execution workspace folder to simulate heavy infrastructure audits:
```text
[TIMESTAMP: 2026-10-01]
RESOURCE: compute_engine_instance_prod_db | SKU: e2-standard-8 | COST: $240.00 | STATUS: RUNNING (Idle 85%)
RESOURCE: bigquery_dataset_analytics | SKU: storage_standard | COST: $145.00 | STATUS: ACTIVE
RESOURCE: unattached_persistent_disk_99 | SKU: pd-ssd | COST: $85.00 | STATUS: UNATTACHED (WASTE)
RESOURCE: cloud_run_staging_api | SKU: vcpu_duration | COST: $12.00 | STATUS: IDLE (Scale to 0 Active)
Total Estimated Unnecessary Spend: $85.00 (Actionable)
```

#### Example UI Execution Prompt Stream
```text
User: Can you read the gcp_cost_export.log file, tell me where we are wasting money, and suggest an architectural fix?

-> Status Spinner: 🛠️ Agent invoking tool: `analyze_local_cost_logs` with args: {'filename': 'gcp_cost_export.log'}
-> Status Code: Success. File bytes analyzed smoothly.

Agent: Based on the workspace cost logs read, you are suffering from a clear infrastructure leakage on 'unattached_persistent_disk_99' incurring a waste of \$85. I recommend setting up an immediate automated cleanup policy via HashiCorp Terraform modules or manual asset detachment to save cloud budget space.
```