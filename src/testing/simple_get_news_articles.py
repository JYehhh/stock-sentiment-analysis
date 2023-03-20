from newspaper import Source
import sys

def scrape_titles(website_url):
    source = Source(website_url)
    source.download()
    source.parse()
    source.set_categories()
    source.build()

    article_urls = source.article_urls()

    titles = []
    for url in article_urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            titles.append(article.title)
        except Exception as e:
            print(f"Error downloading/parsing article: {url}, {str(e)}")

    return titles

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <website_url>")
        sys.exit(1)

    website_url = sys.argv[1]
    titles = scrape_titles(website_url)

    print("Article Titles:")
    for title in titles:
        print(title)