#------------ Final Project -----------
#author: Georgios Akritidis 

import os
import time
import sys
import tweepy
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Stream 
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob 
import matplotlib.pyplot as plt 
import re

consumer_key = 'KOVfNeNA2RHHFNTIinikIb7jM'
consumer_secret = 'SCJyfWKths3MJTbfsTw6kRFzB21BrG76jcgVtyuXNX4DOE33xu'
access_token = '793215429934219264-T05LCEb4RdsGLXWa41s9Jqp7oCToH3F'
access_secret = 'GkIz2CSwkXn1OzoGYS52EPhtspuW6L4bMqcsBkz0IBbeV'
	
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('last jedi')


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")


