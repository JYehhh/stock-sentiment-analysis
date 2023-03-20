from transformers import pipeline

class SentimentAnalyser:
    @staticmethod
    def analyse(articles):
        sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", revision="af0f99b")

        analysed_articles = []

        for article in articles:
            title = ' '.join(article['title'])
            text = ' '.join(article['text'])
            article_text = title + ' ' + text

            sentiment = sentiment_pipeline(article_text)[0]
            sentiment_score = sentiment['score'] if sentiment['label'] == 'POSITIVE' else -sentiment['score']

            analysed_articles.append({
                'title': title,
                'sentiment_score': sentiment_score
            })

        return analysed_articles