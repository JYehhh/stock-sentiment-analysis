from classes.news_article_factory import NewsArticleFactory
import util.stub_dataset
from classes.preprocessor import Preprocessor
from classes.sentiment_analysis import SentimentAnalyser

def process_articles(stock_name, websites):
    # GENERATE ARTICLES
    unprocessed_articles = NewsArticleFactory.generate_articles(stock_name, websites)

    # PREPROCESS ARTICLES
    preprocessed_articles = []
    for article in unprocessed_articles:
        preprocessed_article = Preprocessor.preprocess(article)
        preprocessed_articles.append(preprocessed_article)

    analysed_articles = SentimentAnalyser.analyse(preprocessed_articles)

    return analysed_articles