# import asyncio
from fin_scraper import FinViz
from tweet_screener import Tweets

# odl = FinViz()



# def runner():
new_ = FinViz()
tickers = {}
tickers = new_.pattern_one()
print(tickers , "this is the ticker dict")
for ticker ,price in tickers.items():
    print(ticker ,"this is th key from items pulled")
# # yodl = Tweets("$AAPL")
    yodl = Tweets(ticker)
    yodl.main()
