import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf
from tqdm.notebook import tqdm
import numpy as np
import matplotlib.pyplot as plt

def retrieve_stock_data(symbol):
    print(f'Collecting stock data for {symbol}...')
    stock_info = yf.download(symbol, period="max")
    stock_info = stock_info[['Close']]
    return stock_info

def retrieve_news(symbol):
    print(f'Collecting news for {symbol}...')
    columns = ['date_time', 'symbol', 'news_source', 'news_title']
    news_df = pd.DataFrame(columns=columns)
    article_count = 0
    symbol = str(symbol).lower()
    print("Retrieving news headlines...")

    for page_num in tqdm(range(1, 10)):
        news_url = f'https://twitter.com/news/{symbol}-stock?p={page_num}'
        response = requests.get(news_url)
        webpage_content = response.text
        soup = BeautifulSoup(webpage_content, 'lxml')
        news_articles = soup.find_all('div', class_='latest-news__story')

        for article in news_articles:
            news_datetime = article.find('time', class_='latest-news__date').get('datetime')
            news_title = article.find('a', class_='news-link').text
            news_source = article.find('span', class_='latest-news__source').text
            news_df = pd.concat([pd.DataFrame([[news_datetime, symbol, news_source, news_title]], columns=news_df.columns), news_df], ignore_index=True)
            article_count += 1

    news_df['date_time'] = pd.to_datetime(news_df['date_time'])
    news_df['date'] = news_df['date_time'].dt.date
    news_df['time'] = news_df['date_time'].dt.time
    news_df.drop(columns=['date_time'], inplace=True)
    print(f'{article_count} headlines retrieved from {page_num+1} pages')
    return news_df
