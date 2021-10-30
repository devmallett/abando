# from main import StockResearch.pull_macd
import requests


def test_pull_macd():
    response = requests.get(f'https://www.alphavantage.co/query?function=MACD&symbol=IBM&interval=1min&series_type=open&apikey=demo')
    assert response.status_code == 200