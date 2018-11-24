import time
import re
import requests
from bs4 import BeautifulSoup

def fetch_xml(country_code):
    try: 
        url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={country_code}"
        response = requests.get(url)
        return response.content
    except requests.exceptions.ConnectionError:
        print("failed to connect")

def trends_retriever(country_code):
    """Parses the Google Trends RSS feed using BeautifulSoup.

    Returns:
        dict: Trend title for key, trend approximate traffic for value.
    """
    xml_document = fetch_xml(country_code) 
    soup = BeautifulSoup(xml_document, "lxml")
    titles = soup.find_all("title")
    approximate_traffic = soup.find_all("ht:approx_traffic")
    return {title.text: re.sub("[+,]", "", traffic.text)
            for title, traffic in zip(titles[1:], approximate_traffic)}

if __name__ == "__main__":
    trends = trends_retriever("US")
    print(trends)