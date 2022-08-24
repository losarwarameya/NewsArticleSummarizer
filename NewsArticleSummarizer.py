import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# nltk.download('punkt')


def summarize():

    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publishDate.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publishDate.delete('1.0', 'end')
    publishDate.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publishDate.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    # print(f'Title: {article.title}')
    # print(f'Author(s): {article.authors}')
    # print(f'Publication date: {article.publish_date}')
    # print(f'Summary: {article.summary}')

    # print(analysis.polarity)
    # print(f'Sentiment: {"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')


# gui
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=100)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=100)
author.config(state='disabled', bg='#dddddd')
author.pack()

pdlabel = tk.Label(root, text="Publication Date")
pdlabel.pack()

publishDate = tk.Text(root, height=1, width=100)
publishDate.config(state='disabled', bg='#dddddd')
publishDate.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=100)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=100)
# author.config(state='disabled', bg='#dddddd')
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()


root.mainloop()
