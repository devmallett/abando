import requests
import json
import datetime
# import pandas as pd
# from secrets import TWITTER_API
# from secrets import TWITTER_API_KEY_SECRET
from secrets import TWITTER_BEARER_TOKEN
# from secrets import TWITTER_ACCESS_TOKEN
# from secrets import TWITTER_ACCESS_TOKEN_SECRET
# from fin_scraper import FinViz



#TODO
#call a FinVIz pattern and return the tickers, then use the tickers in an api call to pull tickers associated with the tickers 
#Big TODO - associate tickers with tweets 
"""

"""

class Tweets:
    def __init__(self ,ticker):
        self.ticker = ticker
        self.bearer_token = TWITTER_BEARER_TOKEN
        self.tweet_list = []

    def create_url(self):
        # for ticker ,price in this_ticker.items():
        #     print(ticker ,"this is th key from items pulled")
            
            print("URL was created")
            return "https://api.twitter.com/2/tweets/search/recent?query={}".format(self.ticker)
            
            # return "https://api.twitter.com/2/tweets/search/recent?query=AAPL"
            



    def bearer_oauth(self ,r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = "Bearer {}".format(self.bearer_token)
        # r.headers["User-Agent"] = "v2SampledStreamPython"
        return r


    def connect_to_endpoint(self ,url):
        response = requests.request("GET", url, auth=self.bearer_oauth)
        print(response.status_code)
        for response_line in response.iter_lines(): 
                if response_line:
                    json_response = json.loads(response_line)
                    self.tweet_list = json_response['data']
                    #TODO 
                    # loop through an array of objects to pull text from each object
                    for each_item in self.tweet_list:
                        for tweet_key ,tweet_val in each_item.items():
                            if tweet_key == 'text':
                                # print("{} : {}".format(key, val))
                                print(tweet_val)
                                # tweet_list.append(val)
                                # print(tweet_list)
                                
                            # print("{} : {}".format(key, val))
                        # print(tweet_list[each_item]['text'])
                    
                    
                    
                    
                    # for tweet in json_response['data']:
                    #     print(json_response['data'])
                    # print(json.dumps(json_response, indent=4, sort_keys=True))
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )


    def main(self):
        url = self.create_url()
        # timeout = 0
        now = datetime.datetime.now()
        timeout = now + datetime.timedelta(10)
        # while True:
        if now < timeout:
            self.connect_to_endpoint(url)
            # timeout += 1


    if __name__ == "__main__":
        print("This works")
        main()
        
        
        
  
    

