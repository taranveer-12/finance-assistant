import streamlit as st
import requests
from voice_output import speak

st.title("Finance Assistant")

if st.button("Get Market Brief"):
    res = requests.get("http://localhost:8000/get_brief")
    brief = res.json()["brief"]
    st.write(brief)
    speak(brief)
