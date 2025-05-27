import yfinance as yf

def get_stock_summary(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="2d")
    if len(hist) < 2:
        return "Not enough data."
    today_price = hist['Close'].iloc[-1]
    yesterday_price = hist['Close'].iloc[-2]
    change = round((today_price - yesterday_price) / yesterday_price * 100, 2)
    return f"{ticker} is at ${today_price:.2f}, changed {change}% since yesterday."
