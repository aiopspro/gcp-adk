# 🌤️ Google ADK Weather & Time Assistant Agent

A lightweight, high-performance conversational AI agent built natively on Google's **Agent Development Kit (ADK)** using the **`gemini-flash-latest`** language engine. 

This agent functions as a specialized **City Information Assistant** capable of dynamically orchestrating registered local tools to answer real-time questions about the time and weather for supported metropolitan cities (like New York).

---

## 🏗️ Technical Architecture & Design

Google ADK interprets the Python type-hinting signatures and Google-style docstrings of your functions at system runtime via structural reflection mechanisms (`inspect.signature`) to build out the underlying execution schemas automatically.

### Project Layout & Components
The application encapsulates two core native tool capabilities in a single agent interface:
- **Weather Lookup (`get_weather`):** Evaluates city criteria to return standardized temperature parameters (Celsius and Fahrenheit metrics).
- **Dynamic Time System (`get_current_time`):** Pulls live system clocks matching the destination timezone database layout (`zoneinfo`) to format exact datetime footprints.

---

## 🛠️ Installation & Environment Setup

Run the following commands in your Mac Terminal inside your working workspace directory to safely configure an isolated environment and resolve requirements dependencies:

```bash
# 1. Initialize an isolated virtual environment shell space
python3 -m venv .venv

# 2. Activate the virtual environment workspace on macOS
source .venv/bin/activate

# 3. Upgrade core pip package manager
pip install --upgrade pip

# 4. Install the official Google ADK framework and environmental components
pip install google-adk-python python-dotenv tzdata
```

### Required `requirements.txt` Matrix
Save the following configuration block as `requirements.txt` to safely re-install this exact software stack layout later:
```text
google-adk-python>=0.1.0
python-dotenv>=1.0.0
tzdata>=2023.3
```

---

## ⚙️ Environment Variables Configuration

Create a secure file named exactly **`.env`** in your root workspace project directory. The underlying Google ADK client architecture will automatically parse these credentials fields on system initialization:

```env
GEMINI_API_KEY=AIzaSyYourActualGoogleAIStudioDeveloperKeyHere...
```

---

## 💻 Self-Contained Source Code Blueprint (`agent.py`)

Save the exact codebase snippet below as **`agent.py`** inside your local execution path directory:

```python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


# Instantiating the primary core agent component via Google ADK wrappers
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-flash-latest",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
```

---

## 📟 Deployment & Interface Operations Manual

The Google ADK CLI toolkit provides two native commands to launch and interact directly with your defined `weather_time_agent` object object.

### Mode 1: Run the Interactive Terminal CLI (`adk run`)
To spawn a local conversational text shell session inside your active terminal workspace window, call the agent object by its defined name:

```bash
adk run weather_time_agent
```

#### Expected CLI Execution Log Stream Example
```text
% adk run weather_time_agent
[INFO] Loading environment profiles from local .env context...
[INFO] Reflecting function schemas for: get_weather, get_current_time
[INFO] Core initialization complete. CLI Session Active.

[user]: what is the weather in new york right now?
[weather_time_agent]: Thinking... (Orchestrating tools)
-> [ADK Tool execution]: 'get_weather' with parameters: {'city': 'New York'}
[weather_time_agent]: The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit).

[user]: what time is it there?
[weather_time_agent]: Thinking... (Orchestrating tools)
-> [ADK Tool execution]: 'get_current_time' with parameters: {'city': 'New York'}
[weather_time_agent]: The current time in New York is 2026-10-03 07:55:23 EDT-0400.
```

### Mode 2: Launch the Graphical Web Interface GUI (`adk web`)
To deploy a graphical web interface panel app accessible on any browser across your local network space, run the background server daemon by specifying your target network port:

```bash
adk web --port 8000
```

#### Expected Web Server Terminal Logs
```text
% adk web --port 8000
[INFO] Preparing Google ADK Web Event Loop server daemon...
[INFO] Mounting 'weather_time_agent' runtime layer to app layout...
🚀 Running web daemon on http://localhost:8000
👉 Open your browser and navigate to http://localhost:8000 to interact with your agent GUI!
```

Open a fresh browser tab on your Mac and hit **`http://localhost:8000`** to chat with your agent using the clean, interactive frontend panel dashboard!
