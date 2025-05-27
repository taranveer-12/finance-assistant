import streamlit as st
from get_stock_data import get_stock_summary
from get_news import get_top_news
from retriever import retrieve_insights
from summarize import make_summary
# from voice_output import speak

st.title("🎤 Finance Assistant")

if st.button("🧾 Get Market Brief"):
    # Run agents directly (no FastAPI needed)
    stock_info = get_stock_summary("TSMC")
    news = get_top_news("TSMC")
    filtered_news = retrieve_insights(news, "earnings")
    brief = make_summary(stock_info, filtered_news)
    st.write(brief)
        # speak(brief)


