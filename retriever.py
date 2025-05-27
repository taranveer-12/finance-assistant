def retrieve_insights(news_list, query):
    results = []
    for line in news_list:
        if query.lower() in line.lower():
            results.append(line)
    return results if results else ["No related news found."]
