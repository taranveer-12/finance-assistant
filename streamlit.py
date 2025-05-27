import streamlit as st
import streamlit as st
import requests
# from voice_output import speak

st.title("Finance Assistant")

if st.button("Get Market Brief"):
    res = requests.get("https://81cf264f-a7d7-4b69-8e99-d4480d0e6b4c-00-16tl7qypey0hq.pike.replit.dev/get_brief")  
    brief = res.json()["brief"]
    st.write(brief)
    # speak(brief)

    

