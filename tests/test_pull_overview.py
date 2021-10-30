# from main import StockResearch.pull_macd
import requests


def test_pull_overview():
    response = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo')
    assert response.status_code == 200