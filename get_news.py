import requests
from bs4 import BeautifulSoup

def get_top_news(keyword):
    url = f"https://news.google.com/search?q={keyword}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all("a", class_="DY5T1d")
    headlines = [n.get_text() for n in news[:5]]
    return headlines
