# Stock Analysis and Sentiment Trading Strategy

This repository contains Python scripts and an IPython notebook for analyzing stock prices and implementing a sentiment-based trading strategy using news headlines and Twitter data.

## Table of Contents

1. [Python Scripts](#python-scripts)
   - [Script A: Stock Data and News Retrieval](#script-a-stock-data-and-news-retrieval)
   - [Script B: Trading Simulation](#script-b-trading-simulation)
2. [IPython Notebook](#ipython-notebook)

## Python Scripts

### Script A: Stock Data and News Retrieval

This script contains functions to fetch stock data and related news headlines for a given stock symbol.

#### Dependencies

- requests
- BeautifulSoup
- pandas
- yfinance
- tqdm
- numpy
- matplotlib

#### Functions

- `retrieve_stock_data(symbol)`: Fetches and returns the historical stock prices for the given symbol.
- `retrieve_news(symbol)`: Scrapes and returns news headlines related to the given stock symbol.

### Script B: Trading Simulation

This script simulates trading strategies based on provided trading signals and calculates various performance metrics.

#### Dependencies

- BeautifulSoup
- requests
- pandas
- yfinance
- tqdm
- numpy
- matplotlib

#### Functions

- `simulate_trades(stock_data, trading_signals, capital)`: Simulates trades based on trading signals and calculates the portfolio performance.

## IPython Notebook

The IPython notebook performs a detailed analysis of stock prices and sentiment data from tweets. It includes data cleaning, sentiment analysis, and training machine learning models to predict trading signals.

#### Dependencies

- csv
- pandas
- matplotlib
- math
- time
- pickle
- sklearn
- tqdm
- statsmodels
- re
- numpy
- datetime
- nltk
- unicodedata
- warnings
- textblob

#### Steps

1. **Data Loading and Cleaning**:
   - Load stock and tweet datasets.
   - Combine and clean tweet texts.
   - Perform sentiment analysis using TextBlob and VADER from NLTK.

2. **Sentiment Analysis**:
   - Define and calculate subjectivity and polarity of tweets using TextBlob.
   - Perform VADER sentiment analysis to obtain compound, negative, neutral, and positive scores.

3. **Data Merging**:
   - Merge stock data with tweet sentiment data based on date.
   - Binarize the compound score for use in trading strategy.

4. **Model Training**:
   - Split data into training and testing sets.
   - Train XGBoost and Logistic Regression models to predict sentiment-based trading signals.

5. **Model Evaluation**:
   - Evaluate models using accuracy, precision, recall, F1 score, and ROC AUC score.
   - Plot ROC curves for model performance visualization.

6. **Trading Strategy Simulation**:
   - Identify buy and sell points based on sentiment signals.
   - Calculate returns and cumulative returns for the strategy.
   - Plot cumulative returns for comparison between sentiment strategy and buy-and-hold strategy.

7. **Performance Metrics**:
   - Calculate Sharpe ratio, maximum drawdown, number of trades executed, and win ratio to assess the trading strategy's performance.
