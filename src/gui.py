from main import process_articles
import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the checkboxes
        checkbox_frame = ttk.LabelFrame(self.master, text="Select websites")
        checkbox_frame.grid(column=0, row=0, padx=10, pady=10)

        # Add checkboxes for the websites
        websites = ["Bloomberg", "Forbes", "Sydney Morning Herald", "New York Times", "News.com.au"]
        self.website_vars = {website: tk.BooleanVar() for website in websites}

        for i, website in enumerate(websites):
            chk = ttk.Checkbutton(checkbox_frame, text=website, variable=self.website_vars[website])
            chk.grid(column=i % 2, row=i // 2, padx=10, pady=10)

        # Add a text box for the search phrase
        search_phrase_label = ttk.Label(self.master, text="Enter search phrase:")
        search_phrase_label.grid(column=0, row=1, padx=10, pady=(0, 10), sticky="W")
        self.search_phrase_entry = ttk.Entry(self.master, width=30)
        self.search_phrase_entry.grid(column=0, row=2, padx=10, pady=(0, 10), sticky="W")

        # Add a run button
        run_button = ttk.Button(self.master, text="Run", command=self.on_run_button_click)
        run_button.grid(column=0, row=3, padx=10, pady=10)

    def on_run_button_click(self):
        selected_websites = [website for website in self.website_vars if self.website_vars[website].get()]
        search_phrase = self.search_phrase_entry.get()
        print(f"Selected websites: {selected_websites}")
        print(f"Search phrase: {search_phrase}")

        analysed_articles = process_articles(search_phrase, selected_websites)

        # Display results
        self.display_results(analysed_articles)

    def display_results(self, analysed_articles):
        result_window = tk.Toplevel(root)
        result_window.title("Results")

        num_articles = len(analysed_articles)

        if num_articles == 0:
            no_articles_label = ttk.Label(result_window, text="0 Articles Found, may be because of rate limiting")
            no_articles_label.grid(column=0, row=0, padx=10, pady=10)
        else:
            avg_sentiment = sum([article["sentiment_score"] for article in analysed_articles]) / num_articles

            summary_label = ttk.Label(result_window, text=f"Number of articles: {num_articles}\nAverage sentiment: {avg_sentiment:.6f}")
            summary_label.grid(column=0, row=0, padx=10, pady=10)

            # Discrete sentiment score
            discrete_sentiment = ""
            if avg_sentiment >= 0.7:
                discrete_sentiment = "VERY GOOD"
            elif avg_sentiment >= 0.3:
                discrete_sentiment = "GOOD"
            elif avg_sentiment >= -0.3:
                discrete_sentiment = "OKAY"
            elif avg_sentiment >= -0.7:
                discrete_sentiment = "BAD"
            else:
                discrete_sentiment = "VERY BAD"

            discrete_sentiment_label = ttk.Label(result_window, text=f"Discrete sentiment: {discrete_sentiment}")
            discrete_sentiment_label.grid(column=0, row=1, padx=10, pady=10)

            # List of article titles and their corresponding sentiment scores
            article_list = ttk.LabelFrame(result_window, text="Article Titles and Sentiment Scores")
            article_list.grid(column=0, row=2, padx=10, pady=10)

            for i, article in enumerate(analysed_articles):
                article_title_label = ttk.Label(article_list, text=f"Title: {article['title']}")
                article_title_label.grid(column=0, row=i, padx=10, pady=(0, 10), sticky="W")

                sentiment_score_label = ttk.Label(article_list, text=f"Sentiment Score: {article['sentiment_score']:.6f}")
                sentiment_score_label.grid(column=1, row=i, padx=10, pady=(0, 10), sticky="W")

        close_button = ttk.Button(result_window, text="Close", command=result_window.destroy)
        close_button.grid(column=0, row=3, padx=10, pady=10)

root = tk.Tk()
root.title("Website Sentiment Analysis")
app = Application(master=root)
app.mainloop()