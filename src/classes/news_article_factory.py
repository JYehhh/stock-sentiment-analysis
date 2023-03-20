from newspaper import Article, Source
import concurrent.futures
import random
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import util.stub_dataset as stub

use_stub = True

class NewsArticleFactory:
    @staticmethod
    def generate_articles(stock_name, websites):
        if use_stub == True:
            return stub.get_medium_stub_dataset_ms()

        articles = []
        for w in websites:
            articles.extend(NewsArticleFactory.scrape_website(stock_name, w))

        return articles

    @staticmethod
    def scrape_website(stock_name, site_name):
        website_url = NewsArticleFactory.get_website_url(site_name)
        source = Source(website_url)
        source.download()
        source.parse()
        source.set_categories()
        source.build()

        article_urls = source.article_urls()
        temp_articles = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for url in article_urls:
                futures.append(executor.submit(NewsArticleFactory.process_article, url))

            for future in concurrent.futures.as_completed(futures):
                try:
                    article_data = future.result()
                    if article_data and (stock_name in article_data['title'] or stock_name in article_data['text']):
                        print("Article Found!")
                        temp_articles.append(article_data)
                except Exception as e:
                    url = future_to_url[future]
                    print(f"Error processing article: {url}, {str(e)}")

        return temp_articles
    
    @staticmethod
    def process_article(url):
        print("processing article!")
        # Create a fake UserAgent instance
        user_agent = UserAgent()

        try:
            headers = {'User-Agent': user_agent.random}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else ""
            text = soup.get_text()

            print(title)

            article_data = {
                'title': title,
                'text': text,
            }
            return article_data
        except Exception as e:
            print(f"Error downloading/parsing article: {url}, {str(e)}")
            return None

    @staticmethod
    def get_website_url(site_name):
        if site_name == "Bloomberg": return "https://www.bloomberg.com/"
        if site_name == "Forbes": return "https://www.forbes.com/"
        if site_name == "Sydney Morning Herald": return "https://www.smh.com.au/"
        if site_name == "New York Times":  return "https://www.nytimes.com/"
        if site_name == "News.com.au": return "https://www.news.com.au/"
        else:
            raise Exception("Error: One or More Websites Not Found")
