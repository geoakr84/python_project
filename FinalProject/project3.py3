from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob 
import matplotlib.pyplot as plt
import re
import time

def calctime(a):
	return time.time()-a

positive=0
negative=0
compound=0

count=0
initime = time.time()
plt.ion()

consumer_key = 'KOVfNeNA2RHHFNTIinikIb7jM'
consumer_secret = 'SCJyfWKths3MJTbfsTw6kRFzB21BrG76jcgVtyuXNX4DOE33xu'
access_token = '793215429934219264-T05LCEb4RdsGLXWa41s9Jqp7oCToH3F'
access_secret = 'GkIz2CSwkXn1OzoGYS52EPhtspuW6L4bMqcsBkz0IBbeV'

class listener(StreamListener):

	def on_data(self,data):
		global initime
		t= int(calctime(initime))
		all_data= json.loads(data)
		tweet= all_data['text'].encode('utf-8')
		#tweet2='\n'.join(re.findall(r'[a-zA-Z]+',tweet))
		blob= TextBlob(tweet.strip())

		global positive
		global negative
		global compound
		global count

		count = count + 1
		senti = 0
		for sen in blob.sentences:
			senti = senti + sen.sentiment.polarity
			if sen.sentiment.polarity >= 0:
				positive = positive + sen.sentiment.polarity
			else:
				negative = negative + sen.sentiment.polarity
		compound = compound + senti
		print(count)
		print(tweet.strip())
		print(senti)
		print(t)
		print(str(positive)+ ' ' + str(negative) + ' ' + str(compound))

		plt.axis([0, 70, -20, 20])
		plt.xlabel('Time')
		plt.ylabel('Sentiment')
		plt.plot([t],[positive],'go',[t],[negative],'ro',[t],[compound],'bo')
		plt.show()
		plt.pause(0.0001)
		if count == 200:
			return False
		else:
			return True


	def on_error(self, status):
		print(status)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener(count))
twitterStream.filter(track=["lastJedi"])

#api = tweepy.API(auth)


