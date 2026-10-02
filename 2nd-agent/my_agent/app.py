import streamlit as st
from agent import OpenAIAgent, get_current_time

st.set_page_config(page_title="Agent Web UI", page_icon="🤖")
st.title("🚀 o3-mini AI Agent Dashboard")
st.caption("Running seamlessly on Web GUI Mode")

@st.cache_resource
def load_gui_agent():
    return OpenAIAgent(
        model='o3-mini', name='root_agent', execution_mode="gui",
        instruction="You are a helpful assistant that tells the time. Use 'get_current_time' tool.",
        tools=[get_current_time]
    )

gui_agent = load_gui_agent()

if "gui_messages" not in st.session_state:
    st.session_state.gui_messages = [{"role": "system", "content": gui_agent.instruction}]
if "display_history" not in st.session_state:
    st.session_state.display_history = []

for msg in st.session_state.display_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_query := st.chat_input("Ask about the time..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.display_history.append({"role": "user", "content": user_query})
    
    with st.chat_message("assistant"):
        with st.spinner("o3-mini reasoning..."):
            resp = gui_agent.run(user_query, st.session_state.gui_messages)
            st.markdown(resp)
    st.session_state.display_history.append({"role": "assistant", "content": resp})
