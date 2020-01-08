import twitter
import tweepy
from tweepy import Stream 
from tweepy.streaming import StreamListener
import csv #Import csv
from tweepy import API
from tweepy import OAuthHandler
from textblob import TextBlob
import numpy as np

consumer_key = 'KOVfNeNA2RHHFNTIinikIb7jM'
consumer_secret = 'SCJyfWKths3MJTbfsTw6kRFzB21BrG76jcgVtyuXNX4DOE33xu'
access_token = '793215429934219264-T05LCEb4RdsGLXWa41s9Jqp7oCToH3F'
access_secret = 'GkIz2CSwkXn1OzoGYS52EPhtspuW6L4bMqcsBkz0IBbeV'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#Error handling
if (not api):
    print ("Problem connecting to API")

query=['Star wars: The Last Jedi']
max_tweets = 100

searched_tweets = []
last_id = -1

file = open('result.csv', 'w+')

while len(searched_tweets) < max_tweets:
	count = max_tweets - len(searched_tweets)
	try:
	    new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1), lang="en")
	    if not new_tweets:
	        break
	    searched_tweets.extend(new_tweets)
	    last_id = new_tweets[-1].id
	except tweepy.TweepError as e:
	    break

counter=0
l1=[]
l2=[]
srtl1=[]
srtl2=[]
l3=[]

for tw in searched_tweets:
	print(tw.text)
	analysis = TextBlob(tw.text)
	print(analysis.sentiment)
	print("")	
	l1.append(analysis.sentiment.polarity) 
	l2.append(analysis.sentiment.subjectivity)
	srtl1 = sorted(l1)
	srtl2 = sorted(l2)
	l3 = zip(srtl1, srtl2)
	with open('result.csv', 'w') as file:
		mywriter = csv.writer(file)
		for d in l3:
			mywriter.writerow(d) 			 
	counter = counter + 1

neglist=[]
poslist=[]
neulist=[]

objlist=[]
sublist=[]

for p in l1:
	if p > 0:
		poslist.append(p)
	elif p < 0:
		neglist.append(p)
	else:
		neulist.append(p)

for s in l2:
	if s > 0.49:
		sublist.append(s)
	else:
		objlist.append(s)

rows = zip(poslist, neulist, neglist)
rows2 = zip(objlist, sublist)

with open("polaritylist.csv", 'w') as file:
	mywriter = csv.writer(file)
	for p in rows:
		mywriter.writerow(p)

with open('subjectivitylist.csv', 'w') as file2:
	mywriter2 = csv.writer(file2)
	for sj in rows2:
		mywriter2.writerow(sj)

print("The mean value of polarity is: ",round(np.mean(l1),4))
print("The mean value of subjectivity is: ",round(np.mean(l2),4))
print("--------------------------------------------------")
print("The variance of polarity is",round(np.var(l1, dtype=np.float64),4))
print("The variance of subjectivity is",round(np.var(l2, dtype=np.float64),4))
print("--------------------------------------------------")
print("The standard deviation of polarity is",round(np.std(l1, dtype=np.float64),4))
print("The standard deviation of subjectivity is",round(np.std(l2, dtype=np.float64),4))
print("--------------------------------------------------")
print("Number of Tweets imported: ", counter)
print("--------------------------------------------------")  
print("File polaritylist is created")
print("File subjectivitylist is created")    


