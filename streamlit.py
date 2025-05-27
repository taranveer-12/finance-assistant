import streamlit as st
import streamlit as st
import requests
# from voice_output import speak

st.title("Finance Assistant")

if st.button("Get Market Brief"):
    res = requests.get("https://replit.com/@veer18singh19/finance-assistant")  
    brief = res.json()["brief"]
    st.write(brief)
    # speak(brief)

    

