import requests
from datetime import datetime, timedelta
import smtplib

# Configuration
CONFIG = {
    "STOCK_NAME": "TSLA",
    "COMPANY_NAME": "Tesla Inc",
    "EMAIL": "olegmaksymych@gmail.com",
    "PASSWORD": "password",
    "STOCK_API_KEY": "5TZLDCHA0KM1AXLF",
    "NEWS_API_KEY": "8bafa726829d46bc91a7ed5dbe181247",
    "STOCK_ENDPOINT": "https://www.alphavantage.co/query",
    "NEWS_ENDPOINT": "https://newsapi.org/v2/everything",
    "PERCENTAGE_THRESHOLD": 5
}

# Get dates
today = datetime.today().strftime('%Y-%m-%d')
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')


# Fetch news articles
def fetch_news():
    """Fetch recent news articles related to the stock."""
    params = {
        "q": CONFIG["STOCK_NAME"],
        "from": yesterday,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": CONFIG["NEWS_API_KEY"]
    }
    response = requests.get(CONFIG["NEWS_ENDPOINT"], params=params)
    return response.json()


# Extract top news articles
def get_top_articles(news_data, num_articles=3):
    """Extract the first `num_articles` freshest articles from news_data."""
    articles = news_data.get("articles", [])[:num_articles]
    return [
        {
            "author": article.get("author", "Unknown Author"),
            "title": article.get("title", "No Title"),
            "description": article.get("description", "No Description"),
            "url": article.get("url", "No URL")
        }
        for article in articles
    ]


# Send news via email
def send_news_email(news_data):
    """Send an email notification with the top news articles."""
    top_articles = get_top_articles(news_data)

    if not top_articles:
        print("No articles to send.")
        return

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(CONFIG["EMAIL"], CONFIG["PASSWORD"])

        for article in top_articles:
            subject = article["title"]
            body = f"{article['author']}\n\n{article['description']}\n\nRead more: {article['url']}"
            message = f"Subject: {subject}\n\n{body}"

            connection.sendmail(
                from_addr=CONFIG["EMAIL"],
                to_addrs="olehmaksymych@icloud.com",
                msg=message.encode("utf-8")
            )
            print(f"Email sent: {subject}")


# Fetch stock data
def fetch_stock_data():
    """Retrieve daily stock prices."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": CONFIG["STOCK_NAME"],
        "apikey": CONFIG["STOCK_API_KEY"]
    }
    response = requests.get(CONFIG["STOCK_ENDPOINT"], params=params)
    return response.json()


# Analyze stock price changes
def check_stock_movement():
    """Check stock price movements and send news if a significant change occurs."""
    stock_data = fetch_stock_data()
    time_series = stock_data.get("Time Series (Daily)", {})
    sorted_dates = sorted(time_series.keys(), reverse=True)

    for i, curr_date in enumerate(sorted_dates[:-1]):
        prev_date = sorted_dates[i + 1]
        curr_close = float(time_series[curr_date]["4. close"])
        prev_close = float(time_series[prev_date]["4. close"])
        change_percentage = ((curr_close - prev_close) / prev_close) * 100

        if abs(change_percentage) >= CONFIG["PERCENTAGE_THRESHOLD"]:
            print(f"📈 Significant change on {curr_date}: {change_percentage:.2f}%")
            send_news_email(fetch_news())
            return

    print("No significant changes detected.")


# Run stock analysis
check_stock_movement()
