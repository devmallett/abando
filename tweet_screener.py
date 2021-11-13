import requests
import json
import datetime
# import pandas as pd
# from secrets import TWITTER_API
# from secrets import TWITTER_API_KEY_SECRET
from secrets import TWITTER_BEARER_TOKEN
# from secrets import TWITTER_ACCESS_TOKEN
# from secrets import TWITTER_ACCESS_TOKEN_SECRET
from fin_scraper import FinViz


new_request = FinViz()

this_ticker = new_request.pattern_one()

bearer_token = TWITTER_BEARER_TOKEN

#TODO
#call a FinVIz pattern and return the tickers, then use the tickers in an api call to pull tickers associated with the tickers 
#Big TODO - associate tickers with tweets 
"""

"""




def create_url():
    # for ticker ,price in this_ticker.items():
    #     print(ticker ,"this is th key from items pulled")
        
        # return "https://api.twitter.com/2/tweets/search/recent?query={}".format(ticker)
        return "https://api.twitter.com/2/tweets/search/recent?query=ROON"



def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = "Bearer {}".format(bearer_token)
    # r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    tweet_list = []
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    for response_line in response.iter_lines(): 
            if response_line:
                json_response = json.loads(response_line)
                tweet_list = json_response['data']
                #TODO 
                # loop through an array of objects to pull text from each object
                for each_item in tweet_list:
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


def main():
    url = create_url()
    # timeout = 0
    now = datetime.datetime.now()
    timeout = now + datetime.timedelta(10)
    # while True:
    if now < timeout:
        connect_to_endpoint(url)
        # timeout += 1


if __name__ == "__main__":
    main()

