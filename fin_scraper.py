import requests
from bs4 import BeautifulSoup
import pandas as pd


# def fin_one():

fin_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
fin_viz_request = requests.get(
    "https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o1000,sh_price_u20,ta_pattern_tlresistance&ft=4", headers=fin_headers).text

pattern_one = pd.read_html(fin_viz_request)
pattern_one = pattern_one[-2]
pattern_one.columns = pattern_one.iloc[0]
pattern_one = pattern_one[1:]
cols = [1 ,8]
iso = pattern_one[pattern_one.columns[cols]]


#TODO
#return ticker and prices that are higher than 15 dollars


for price in range(1 ,len(iso["Price"])):
    if int(float(iso["Price"][price])) > 15:
        print(iso["Price"][price])


# print(iso["Price"][1])
    



# print(iso)
