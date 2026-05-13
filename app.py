import streamlit as st
import requests
import os
import json


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://vaultiq-backend-mluv.onrender.com"
).rstrip("/")

st.set_page_config(
    page_title="VaultIQ",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>


[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        120deg,
        #f8ebf5 0%,
        #f3f2ff 35%,
        #e8f7ff 70%,
        #edfff6 100%
    );
}


#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}


[data-testid="stSidebar"] {
    background: #f8f8fc;
    border-right: 1px solid #ececec;
}


.app-title {
    font-size: 28px;
    font-weight: 700;
}


.new-chat-btn button {
    width:100%;
    border:none;
    border-radius:18px;
    background: linear-gradient(90deg,#8b5cf6,#22c1f1);
    color:white;
    font-weight:600;
    height:50px;
}


.hero-title {
    text-align:center;
    font-size:64px;
    font-weight:800;
    color:#111827;
}

.hero-sub {
    text-align:center;
    color:#5b6170;
    font-size:20px;
    margin-bottom:30px;
}


.suggestion-card button {
    width:100%;
    height:90px;
    border-radius:20px;
    background:white;
    border:none;
    box-shadow:0px 6px 20px rgba(0,0,0,0.05);
}


.file-card {
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.06);
    margin-bottom:15px;
}


.stChatInputContainer {
    position:fixed;
    bottom:20px;
    width:60%;
    left:30%;
    background:white;
    border-radius:25px;
    padding:10px;
    box-shadow:0px 8px 30px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)



if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = []

if "quick_prompt" not in st.session_state:
    st.session_state.quick_prompt = None


with st.sidebar:
    st.markdown(
        """
        <div class="app-title">VaultIQ</div>
        <div style="color:gray;">AI Drive Search</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='new-chat-btn'>", unsafe_allow_html=True)
    if st.button("+ New Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Recent Searches")

    
    if st.session_state.chat_sessions:
        for item in st.session_state.chat_sessions[-10:]:
            st.markdown(f"📄 {item}")
    else:
        st.caption("No recent searches")

    st.markdown("---")
    st.caption("Google Drive Connected")


col1, col2 = st.columns([8,2])

with col1:
    st.markdown("### 📁 Workspace > Personal Drive")

with col2:
    st.success("Connected to Google Drive")


if len(st.session_state.messages) == 0:
    st.markdown("""
        <div class="hero-title">
            Hello 👋
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="hero-sub">
            Search your Google Drive intelligently with AI
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("📄 Find PDFs"):
            st.session_state.quick_prompt = "Find PDFs"

    with c2:
        if st.button("🕒 Recent Documents"):
            st.session_state.quick_prompt = "Recent Documents"

    with c3:
        if st.button("📊 Financial Reports"):
            st.session_state.quick_prompt = "Financial Reports"


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

prompt = None

if st.session_state.quick_prompt:
    prompt = st.session_state.quick_prompt
    st.session_state.quick_prompt = None

user_input = st.chat_input("Ask me to find files...")

if user_input:
    prompt = user_input

if prompt:

    
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.session_state.chat_sessions.append(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Searching your Drive..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={
                        "message": prompt,
                        "history": st.session_state.messages[-4:]
                    },
                    timeout=60
                )

                response.raise_for_status()

                backend_response = response.json()

                
                if isinstance(backend_response, dict):
                    reply = backend_response.get("response", "No response received.")
                else:
                    reply = str(backend_response)

            except requests.exceptions.ConnectionError:
                reply = "❌ Unable to connect to backend."

            except Exception as e:
                reply = f"❌ {str(e)}"

        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })