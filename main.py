from fastapi import FastAPI
from get_stock_data import get_stock_summary
from get_news import get_top_news
from retriever import retrieve_insights
from summarize import make_summary

app = FastAPI()

@app.get("/get_brief")
def get_brief():
    stock_info = get_stock_summary("TSM")
    news = get_top_news("TSMC")
    filtered_news = retrieve_insights(news, "earnings")
    summary = make_summary(stock_info, filtered_news)
    return {"brief": summary}
