import requests
import spacy
import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup

data = requests.get("https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms")

soup = BeautifulSoup(data.content, features='xml')

d = set([tag.name for tag in soup.find_all()])
titles = soup.findAll('title')

nlp = spacy.load('en_core_web_sm')

print(titles[5].text)
proccessed_title = nlp(titles[5].text)

# [print(token.text + "->" + token.pos_ + "->" + token.dep_) for token in proccessed_title]

# Both works in jupyter notebook or g colab. pycharm not supporting for charts.
# spacy.displacy.render(proccessed_title, style='dep', jupyter=True, options={'distance': 120})

# spacy.displacy.render(proccessed_title, style='ent', jupyter=True, options={'distance': 120})

companies = []
for title in titles:
    doc = nlp(title.text)
    for token in doc.ents:
        if token.label_ == 'ORG':
            companies.append(token.text)
        else:
            pass

stocks_df = pd.read_csv('ind_nifty500list.csv')
print(stocks_df.columns.tolist())
## collect various market attributes of a stock
stock_dict = {
    'Org': [],
    'Symbol': [],
    'currentPrice': [],
    'dayHigh': [],
    'dayLow': [],
    'forwardPE': [],
    'dividendYield': []
}

## for each company look it up and gather all market data on it
for company in companies:
    try:
        if stocks_df['Company Name'].str.contains(company).sum():
            print(stocks_df['Company Name'].str.contains(company).sum())
            symbol = stocks_df[stocks_df['Company Name']. \
                str.contains(company)]['Symbol'].values[0]
            org_name = stocks_df[stocks_df['Company Name']. \
                str.contains(company)]['Company Name'].values[0]
            stock_dict['Org'].append(org_name)
            stock_dict['Symbol'].append(symbol)
            stock_info = yf.Ticker(symbol + ".NS").info
            stock_dict['currentPrice'].append(stock_info['currentPrice'])
            stock_dict['dayHigh'].append(stock_info['dayHigh'])
            stock_dict['dayLow'].append(stock_info['dayLow'])
            stock_dict['forwardPE'].append(stock_info['forwardPE'])
            stock_dict['dividendYield'].append(stock_info['dividendYield'])
        else:
            pass
    except:
        pass

## create a dataframe to display the buzzing stocks
stocks = pd.DataFrame(stock_dict)
print(stocks)
