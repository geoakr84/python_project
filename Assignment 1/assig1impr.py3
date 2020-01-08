import re
import string

text = "We have developed speed,  but we have shut ourselves in. Machinery that gives abundance has left us in want. Our knowledge has made us cynical. Our cleverness, hard and unkind. We think too much and feel too little. More than machinery we need humanity. More than cleverness we need kindness and gentleness."
wordlist=[]
wordlist2=[]
numberlist=[]
charlist=[]
charlist2=[]
charnumlist=[]
charnumlist2=[]
charnumlist3=[]
count2=0
maxindex=[]

def countSentences():
	p= re.findall(r'[.!?]',text)
	count = len(p)  #\. count all dots to calculate how many sentences the text has 
	rating=['first','second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
		
	p2= re.findall(r'[.!?]',text)
	wordlist=re.compile('[.!?]').split(text)
	wordlist2=[x for x in wordlist if x != '']
	
	i=0
	for i in range (len(wordlist2)):
		count2=len(re.findall(r'\w+', wordlist2[i]))			
		print("The number of words for the",rating[i],"sentence is: ",count2)
		i=i+1
	return


def countCharacters():
	nodots=re.sub(r'[.,!?;]', '', text)
	charlist=nodots.split()

	for x in charlist:
		if x not in charlist2:
			charlist2.append(x.lower())

	for c in range (len(charlist2)):
		count3=len(re.findall('\S',charlist2[c]))
		charnumlist.append(count3)
	
	

	b=[x[0] for x in sorted(enumerate(charnumlist), key=lambda x: x[1])[-7:]]
	c=sorted(b, reverse=True)
	
	k=1
	for x in c:
		print("Longest word ",k,": ",charlist2[x])
		k=k+1
	

	print("=========================================")
	m=sorted(charnumlist, reverse=True)
	m2=[10,9]
	
	for i, elem in enumerate(charnumlist):
		if elem in m2:
			charnumlist2.append(i)
	
	y=1
	charnumlist3=sorted(charnumlist2, reverse=True)
	
	for x in charnumlist3:
		print("Longest word ",y,": ",charlist2[x])
		y=y+1

	
		


	

countSentences()
print("====================================")
countCharacters()