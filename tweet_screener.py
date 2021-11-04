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

bearer_token = TWITTER_BEARER_TOKEN

#TODO
#call a FinVIz pattern and return the tickers, then use the tickers in an api call to pull tickers associated with the tickers 
#Big TODO - associate tickers with tweets 
"""
lets think about this 
your end goal is to get 10 tweets associated with a ticker 
right now you have 10 tweets associated with one ticker 
ticker is hard coded
you want to be able to bring the ticker from the finviz call and run it through the tweet screener
thing is you dont want to do that in the tweet screener - you need an agreggator class that pulls from both apis
you would still have to call the finviz api first to recieve the ticker 
once you get the ticker you would have to run the ticker through the twitter class 
first start by makign the tweet call into its own class


"""


def create_url():
    return "https://api.twitter.com/2/tweets/search/recent?query=ABCL"



def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = "Bearer {}".format(bearer_token)
    # r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    for response_line in response.iter_lines(): 
            if response_line:
                json_response = json.loads(response_line)
                tweet_list = json_response['data']
                #TODO 
                # loop through an array of objects to pull text from each object
                for each_item in tweet_list:
                    for key ,val in each_item.items():
                        if key == 'text':
                            # print("{} : {}".format(key, val))
                            print(val)
                            
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
    timeout = now + datetime.timedelta(3)
    # while True:
    if now < timeout:
        connect_to_endpoint(url)
        # timeout += 1


if __name__ == "__main__":
    main()

