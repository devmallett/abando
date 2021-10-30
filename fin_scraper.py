import requests
from bs4 import BeautifulSoup
import pandas as pd


# main = 'https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o1000,sh_price_u20,ta_pattern_tlresistance&ft=4' 
#     # links.append(main)
# fin_request = requests.get(main)
# # state_pull = BeautifulSoup(state_request.content ,'html5lib')
# soup = BeautifulSoup(fin_request.content, 'html5lib')

# print(soup.prettify())
fin_headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# req = requests.get("https://finviz.com/quote.ashx?t=FB" ,headers = headers)
fin_viz_request = requests.get("https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o1000,sh_price_u20,ta_pattern_tlresistance&ft=4" ,headers = fin_headers).text

pattern_one = pd.read_html(fin_viz_request)
pattern_one = pattern_one[-2]
pattern_one.columns = pattern_one.iloc[0]
# pattern_one.columns = pattern_one.loc[[ "Ticker" ] ,["Price"]]
pattern_one = pattern_one[1:]
cols = [1 ,8]
iso = pattern_one[pattern_one.columns[cols]]
# rows = pattern_one.iloc[2:len(pattern_one)]
# rows = pattern_one.columns[[" Ticker "] ,[" Price "]]

print(iso)
# print(pattern_one)




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