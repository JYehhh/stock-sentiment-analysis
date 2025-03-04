# 🙂 Sentiment Analysis for Stock Picks
A Python application that performs sentiment analysis on news articles containing specific company names to assist in stock selection and observe Efficient Market Hypothesis.

## Introduction
This project aims to help users make better stock picks by performing sentiment analysis on news articles related to specific companies. The application scrapes live news articles, searches for mentions of a given company name, and calculates the average sentiment score based on the article content. A user-friendly GUI allows users to input the desired stock and select news sources for analysis, presenting the sentiment score and distribution per news article visually.

**NOTE:** Due to rate limiting issues during web scraping, the current implementation uses a stub dataset as a workaround. If you wish to use the stub dataset, input the stock name as "microsoft" and choose any company. The code is located in news_article_factory.py and the stubbing is controlled by the variable use_stub. To disable stubbing and attempt to scrape articles directly, set use_stub to False.

## Technologies
- Python
- TensorFlow
- Hugging Face Transformers
- Newspaper3k
- Tkinter
- Matplotlib

## Methods
- **Web Scraping:** Efficiently extracting news articles using the Newspaper3k library with techniques such as fake user agents and random time delays to respect website rate limits.
- **Multithreading:** Parallel processing of article scraping and sentiment analysis to speed up the overall process.
- **Sentiment Analysis:** Training a TensorFlow model using the Hugging Face Transformers library for accurate sentiment analysis tailored to the stock market domain.
- **GUI:** Designing a user-friendly interface with Tkinter and Matplotlib to facilitate user interaction and display results.

## Getting Started
Clone the repository to your local machine.

```
git clone https://github.com/JYehhh/sentiment-analysis-stock-picks.git
```

Install the required dependencies.

```
pip install -r requirements.txt
```

## Usage
Run the GUI script.

``` python gui.py```

- Input the stock name and select news sources for analysis in the GUI.
- Review the sentiment score and distribution per news article displayed in the visualizations.
