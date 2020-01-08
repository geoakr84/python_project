import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


consumer_key = 'KOVfNeNA2RHHFNTIinikIb7jM'
consumer_secret = 'SCJyfWKths3MJTbfsTw6kRFzB21BrG76jcgVtyuXNX4DOE33xu'
access_token = '793215429934219264-T05LCEb4RdsGLXWa41s9Jqp7oCToH3F'
access_secret = 'GkIz2CSwkXn1OzoGYS52EPhtspuW6L4bMqcsBkz0IBbeV'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
 
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
 
    twitterStream = Stream(auth, listener)
    twitterStream.filter(track=['#lastjedi'])