from secrets import API_KEY
import requests
import json



class StockResearch:
    def __init__(self ,ticker):
        self.ticker = ticker
        self.base = 'https://www.alphavantage.co/query?'

        

    def pull_macd(self ,interval ,series_type):
        
        url = f'{self.base}function=MACD&symbol={self.ticker}&interval={interval}&series_type={series_type}&apikey={API_KEY}'
        r = requests.get(url)
        data = r.json()

        print(data)
            

    def pull_overview(self):
        url = f'{self.base}function=OVERVIEW&symbol={self.ticker}&apikey={API_KEY}'
        r = requests.get(url)
        data = r.json()
        
        # if data['52WeekLow'] > 100:
        #     print(data['MarketCapitalization'] ,'Market Capitilization')

        print(data['52WeekLow'])
    

testing = StockResearch("IBM")

testing.pull_overview()



