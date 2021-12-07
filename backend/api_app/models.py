from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.
'''
From individual calls 
class Tweets:
    def __init__(self ,ticker):
        self.ticker = ticker
        self.bearer_token = TWITTER_BEARER_TOKEN
        self.tweet_list = []
        
        
class FinViz:
    def __init__(self):
        self.target_cols = [1, 8]
        self.ticker_list = []
        self.price_list = []
        self.pattern_one_dict = {}
        self.pattern_two_dict = {}
        self.pattern_three_dict = {}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}



'''

class Results(models.Model):
    ticker = models.CharField(max_length = 4)
    tweets = models.CharField(
       max_length=32,
       choices=[],  # some list of choices
   )
    price = DecimalField(max_digits = 32 ,decimal_places = 2 ,blank = True ,null = True) 