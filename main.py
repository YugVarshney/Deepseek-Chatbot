import os
import streamlit as st
from dotenv import load_dotenv
import deepseek as ds  

load_dotenv()

st.set_page_config(
    page_title="Chat with DeepSeek!",
    page_icon=":brain:",
    layout="centered",
)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

ds.configure(api_key=DEEPSEEK_API_KEY)
model = ds.GenerativeModel('deepseek-chat')  

def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 DeepSeek - ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask DeepSeek...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    deepseek_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("assistant"):
        st.markdown(deepseek_response.text)
