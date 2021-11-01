import requests
import json
# import pandas as pd
# from secrets import TWITTER_API
# from secrets import TWITTER_API_KEY_SECRET
from secrets import TWITTER_BEARER_TOKEN
# from secrets import TWITTER_ACCESS_TOKEN
# from secrets import TWITTER_ACCESS_TOKEN_SECRET

bearer_token = TWITTER_BEARER_TOKEN


def create_url():
    return "https://api.twitter.com/2/tweets/search/recent?query=eth"



def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    # r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()

