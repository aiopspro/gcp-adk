# 🌍 GCP ADK Mock City Time Checker Agent

A self-contained, high-performance conversational AI agent built using Google's **Agent Development Kit (ADK)** and running on the highly economical, learning-friendly **`gemini-3.5-flash-lite`** engine. 

This repository acts as an optimized baseline for practicing tool registration, structural prompt engineering, and multi-interface layout routing natively inside the Google cloud ecosystem.

---

## 🏗️ Technical Architecture & Cost Controls

Google ADK automatically reads your Python signatures and docstrings via reflection mechanisms (`inspect.signature`) to build out the underlying parameters schemas.

### 📉 Cost Optimization Controls
- **`gemini-3.5-flash-lite` Model:** Bypasses legacy `404 NOT_FOUND` client access errors thrown by older deprecated versions (like 2.5-flash) for fresh billing profile profiles. It executes at Google's absolute lowest pricing tier (~\$0.10 per 1M tokens) to keep your experimental learning runway completely protected.
- **Experimental Introspector:** Hides complex JSON manual payload typing declarations behind the library backend. The system handles all parameter conversions seamlessly out of the box.

---

## 🛠️ Environment & Installation Setup

Execute the following commands in your Mac Terminal inside your working workspace directory to safely configure an isolated environment space:

```bash
# 1. Initialize an isolated virtual environment shell space
python3 -m venv .venv

# 2. Activate the virtual environment workspace on macOS
source .venv/bin/activate

# 3. Upgrade core pip dependencies
pip install --upgrade pip

# 4. Install the official Google ADK frameworks and environment utils
pip install google-adk-python python-dotenv
```

### Required `requirements.txt` Matrix
Save this footprint as `requirements.txt` to safely re-install this exact stack inside another workspace later:
```text
google-adk-python>=0.1.0
python-dotenv>=1.0.0
```

---

## ⚙️ Environment Variables Configuration

Create a secure file named exactly **`.env`** in your root workspace project directory. The Google ADK system architecture will automatically parse these values on boot:

```env
GEMINI_API_KEY=AIzaSyYourActualGoogleAIStudioDeveloperKeyHere...
```

---

## 📟 Production Code Blueprint (`agent.py`)

Save the exact snippet blueprint below as **`agent.py`** inside your directory space:

```python
import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

# Automatically load the credentials from the local environment space
load_dotenv()

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

# Initialize your target Agent exactly inside your GCP ADK workflow!
root_agent = Agent(
    # 👑 THE FIX: Bypasses the 404 block and gives you the cheapest possible Gemini token rates
    model='gemini-3.5-flash-lite',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)
```

---

## 📟 Deployment & Interface Operations Manual

Google ADK gives you two distinct native tools to execute your configuration script objects—the terminal text chat shell and the local network web graphical dashboard.

### Mode 1: Run the Interactive Terminal CLI (`adk run`)
To run a direct text console loop conversation inside your active shell panel workspace, execute:

```bash
adk run root_agent
```

#### Expected CLI Execution Log Stream
```text
% adk run root_agent
[INFO] Parsing environment profiles from local .env space...
[INFO] Reflecting function metadata parameters signature for: get_current_time
[INFO] Initialization complete. Console session active.

[user]: what is time now in delhi
[root_agent]: Thinking... (Evaluating tools)
-> [ADK Tool execution]: 'get_current_time' with parameters: {'city': 'Delhi'}
[root_agent]: The current time in Delhi is 10:30 AM.

[user]: check for berlin as well
[root_agent]: Thinking... (Evaluating tools)
-> [ADK Tool execution]: 'get_current_time' with parameters: {'city': 'Berlin'}
[root_agent]: The current time in Berlin is 10:30 AM.
```

### Mode 2: Launch the Graphical Web Interface GUI (`adk web`)
To deploy a web dashboard application panel accessible on any browser across your local machine, run the server daemon by explicitly allocating the desired network port:

```bash
adk web --port 8000
```

#### Expected Web Server Terminal Logs
```text
% adk web --port 8000
[INFO] Launching Google ADK Web Framework worker process...
[INFO] Attaching 'root_agent' orchestration runtime layer...
🚀 Running web daemon on http://localhost:8000
👉 Open your browser and navigate to http://localhost:8000 to interact with your agent GUI!
```

Open a fresh browser tab window on your Mac, navigate directly to **`http://localhost:8000`**, and you can chat with your agent visually. It will display a drop-down list tracking the tool execution variables whenever you ask about time metrics!
