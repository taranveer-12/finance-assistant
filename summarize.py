def make_summary(stock_info, news_list):
    summary = "Market Brief:\n"
    summary += stock_info + "\n"
    summary += "News Highlights:\n"
    for news in news_list:
        summary += "- " + news + "\n"
    return summary
