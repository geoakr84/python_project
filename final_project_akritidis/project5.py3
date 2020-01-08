import twitter
import tweepy
from tweepy import Stream 
from tweepy.streaming import StreamListener
import csv 
from tweepy import API
from tweepy import OAuthHandler
from textblob import TextBlob
import numpy as np
import re
from itertools import chain

#Below I enter the credentials that I produced in Twitter developers webpage
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

query=['The last jedi'] #the key phrase that will be searched 
max_tweets = 100 #the maximum number of tweets that will be collected

searched_tweets = [] #a list to store the imported tweets
last_id = -1
sinceId = ""

file = open('result.csv', 'w+') 

#the code to import the tweets
while len(searched_tweets) < max_tweets:
	count = max_tweets - len(searched_tweets)
	try:
	    new_tweets = api.search(q=query, count=count, sinceId=str(sinceId), max_id=str(last_id - 1), lang="en")
	    if not new_tweets:
	        break
	    searched_tweets.extend(new_tweets)
	    last_id = new_tweets[-1].id
	except tweepy.TweepError as e:
	    break

l1=[]
l2=[]
srtl1=[]
srtl2=[]
l3=[]
counter = 0

def sentimentAnalysis():
	global counter
	for tw in searched_tweets:
		print(tw.text)
		analysis = TextBlob(tw.text) # here I call the class TextBlob in order to make the sentiment analysis
		print(analysis.sentiment)
		print("")	
		l1.append(analysis.sentiment.polarity) # I store the values of polarity in the list l1
		l2.append(analysis.sentiment.subjectivity) # I store the values of subjectivity in the list l2
		srtl1 = sorted(l1) # I sort the values of the list
		srtl2 = sorted(l2) #  -//-   -//-   -//-   -//-
		l3 = zip(srtl1, srtl2)
		with open('result.csv', 'w') as file: # creation of a file with values of polarity and subjectivity
			mywriter = csv.writer(file)
			for d in l3:
				mywriter.writerow(d) 			 
		counter = counter + 1 # counter to count the number of tweets imported

neglist=[] # creation of an empty list to store the negative values of polarity
poslist=[] # creation of an empty list to store the positive values of polarity
neulist=[] # creation of an empty list to store the values of polarity that are equal to zero

objlist=[] # creation of a list to store the values of subjectivity lower than 0.50 which can be characterized as objective
sublist=[] # creation of a list to store the values of subjectivity greater or equal than 0.50 which can be characterized as subjective

def printFiles():
	for p in l1:
		if p > 0:
			poslist.append(round(p,2))
		elif p < 0:
			neglist.append(round(p,2))
		else:
			neulist.append(round(p,2))

	for s in l2:
		if s > 0.49:
			sublist.append(round(s,2))
		else:
			objlist.append(round(s,2))

	rows = neglist + neulist + poslist

	rows2 = objlist + sublist 

	with open("polaritylist.txt", 'w') as file: # creation of a text file to store the values of polarity
		for i in rows:
			file.write(str(i))
			file.write("\n")

	with open('subjectivitylist.txt', 'w') as file2: # creation of a text file to store the values of subjectivity
		for i in rows2:
			file2.write(str(i))
			file2.write("\n")

links = [] # creation of an empty list to store the text of the tweets
urls = [] # creation of an empty list to store the links that were found inside the text
urls2 = []
unique_list = [] # creation of a list to store the urls without any duplicated
flat_list = []

def printLinks():
	for lk in searched_tweets: # loop to find the text
		txt = lk.text
		links.append(txt)

	for ht in links:
		http = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',ht) # regex to find the urls
		urls.append(http)
	urls2 = [x for x in urls if x != []] # creation of a list to include only the tweets that contained a url and not the rest which are empty
	flat_list = [item for sublist in urls2 for item in sublist] # I store all the urls here
	
	for h in flat_list:
		if h not in unique_list:
			unique_list.append(h)
	with open ('urls.txt', 'w+') as ufile: # creation of a text file to store the unique urls
		for i in unique_list:
			ufile.write(i)
			ufile.write('\n')

	print("Number of urls posted: ",len(flat_list))
	print("Number of unique urls posted: ",len(unique_list))

sentimentAnalysis()
printFiles()
printLinks()

# presentation of statistics regarding the polarity, subjectivity, number of urls and tweets
print("--------------------------------------------------")
print("Number of positive tweets is: ",len(poslist))
print("Number of neutral tweets is: ", len(neulist))
print("Number of negative tweets is: ", len(neglist))
print("--------------------------------------------------")
print("Number of objective tweets is: ", len(objlist))
print("Number of subjective tweets is: ", len(sublist))
print("--------------------------------------------------")
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


