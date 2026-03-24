from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()

chatbot = Groq()
model = "openai/gpt-oss-120b"

# 🎨 Page config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# 💅 Custom CSS (clean + modern)
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.user-msg {
    background-color: #2563EB;
    padding: 10px 15px;
    border-radius: 12px;
    color: white;
    margin: 8px 0;
    text-align: right;
}
.bot-msg {
    background-color: #1F2937;
    padding: 10px 15px;
    border-radius: 12px;
    color: white;
    margin: 8px 0;
    text-align: left;
}
.title {
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🎯 Title only (clean look)
st.markdown('<div class="title">🤖 AI Chat Assistant</div>', unsafe_allow_html=True)

# 🧠 Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🎛️ Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []

    temperature = st.slider("Creativity", 0.0, 1.0, 0.7)

# 🖥️ Chat display
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

# 💬 Input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    st.markdown(f'<div class="user-msg">{user_input}</div>', unsafe_allow_html=True)

    with st.spinner("Thinking..."):
        response = chatbot.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
            temperature=temperature
        )

        reply = response.choices[0].message.content

    # ✨ Smooth typing effect
    placeholder = st.empty()
    typed = ""
    for char in reply:
        typed += char
        placeholder.markdown(f'<div class="bot-msg">{typed}</div>', unsafe_allow_html=True)
        time.sleep(0.01)

    placeholder.markdown(f'<div class="bot-msg">{reply}</div>', unsafe_allow_html=True)

    st.session_state.messages.append({"role": "assistant", "content": reply})