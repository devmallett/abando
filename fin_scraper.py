import requests
from bs4 import BeautifulSoup
import pandas as pd




#TODO
# Abstract logic so that you only have to make function calls within the different patterns 
# Map the keys and vlaues of those tickers and retrun them in a global object 


class FinViz:
    def __init__(self):
        self.target_cols = [1 ,8]
        self.open_list = []
        self.headers = { 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    # def price_logic(self):
    #     iso = ""
    #     for price in range(1 ,len(iso["Price"])): 
    #             if int(float(iso["Price"][price])) > 15:
    #                 self.open_list.append(iso["Price"][price])
    #                 print(self.open_list)
    


    def pattern_one(self):


        fin_viz_request = requests.get(
            "https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o1000,sh_price_u20,ta_pattern_tlresistance&ft=4", headers=self.headers).text

        pattern_one = pd.read_html(fin_viz_request)
        pattern_one = pattern_one[-2]
        pattern_one.columns = pattern_one.iloc[0]
        pattern_one = pattern_one[1:]
        iso = pattern_one[pattern_one.columns[self.target_cols]]

        open_list = []

        for price in range(1 ,len(iso["Price"])): #global in class
            if int(float(iso["Price"][price])) > 15:
                open_list.append(iso["Price"][price])
                print(open_list)

    def pattern_two(self):

        fin_viz_request = requests.get(
            "https://finviz.com/screener.ashx?v=111&f=earningsdate_nextweek,sh_price_u20,ta_pattern_channelup&ft=4", headers=self.headers).text

        pattern_two = pd.read_html(fin_viz_request)
        pattern_two = pattern_two[-2]
        pattern_two.columns = pattern_two.iloc[0]
        pattern_two = pattern_two[1:]
        iso = pattern_two[pattern_two.columns[self.target_cols]]

        open_list = [] #global in calss

        for price in range(1 ,len(iso["Price"])):
            if int(float(iso["Price"][price])) > 15:
                open_list.append(iso["Price"][price])
                print(open_list)


    def pattern_three(self):

        fin_viz_request = requests.get(
            "https://finviz.com/screener.ashx?v=111&f=earningsdate_nextweek,fa_pe_profitable,sh_avgvol_o1000,sh_price_u30,ta_pattern_tlresistance&ft=4", headers=self.headers).text

        pattern_three = pd.read_html(fin_viz_request)
        pattern_three = pattern_three[-2]
        pattern_three.columns = pattern_three.iloc[0]
        pattern_three = pattern_three[1:]
        iso = pattern_three[pattern_three.columns[self.target_cols]]

        open_list = []

        for price in range(1 ,len(iso["Price"])):
            if int(float(iso["Price"][price])) > 15:
                open_list.append(iso["Price"][price])
                print(open_list)

new_request = FinViz()

new_request.pattern_one()
    



# print(iso)
