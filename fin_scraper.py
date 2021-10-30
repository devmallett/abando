import requests
from bs4 import BeautifulSoup
import pandas as pd


# main = 'https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o1000,sh_price_u20,ta_pattern_tlresistance&ft=4' 
#     # links.append(main)
# fin_request = requests.get(main)
# # state_pull = BeautifulSoup(state_request.content ,'html5lib')
# soup = BeautifulSoup(fin_request.content, 'html5lib')

# print(soup.prettify())
headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# req = requests.get("https://finviz.com/quote.ashx?t=FB" ,headers = headers)
req = requests.get("https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o1000,sh_price_u20,ta_pattern_tlresistance&ft=4" ,headers = headers).text

table = pd.read_html(req)



print(table[-2])




# soup = BeautifulSoup(req.content, 'html.parser')
# table = soup.find_all(lambda tag: tag.name=='table')
# rows = table[8].findAll(lambda tag: tag.name=='tr')
# out=[]
# for i in range(len(rows)):
#     td=rows[i].find_all('td')
#     out=out+[x.text for x in td]
#     print(out)

# print(table)
# print(soup.prettify())