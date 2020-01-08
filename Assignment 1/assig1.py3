import re
import string
from heapq import nlargest
import heapq

text = "We have developed speed,  but we have shut ourselves in. Machinery that gives abundance has left us in want. Our knowledge has made us cynical. Our cleverness, hard and unkind. We think too much and feel too little. More than machinery we need humanity. More than cleverness we need kindness and gentleness."


def countWords():
        count2 = len(re.findall(r'\w+', text))  #\w expression to match a single word character
        print("The number of words are: ",count2)
        return

s1= "We have developed speed,  but we have shut ourselves in."
s2= "Machinery that gives abundance has left us in want."
s3= "Our knowledge has made us cynical."
s4= "Our cleverness, hard and unkind."
s5= "We think too much and feel too little."
s6= "More than machinery we need humanity."
s7= "More than cleverness we need kindness and gentleness."
def countWordsinSentences():
	c1= len(re.findall(r'\w+',s1))
	c2= len(re.findall(r'\w+',s2))
	c3= len(re.findall(r'\w+',s3))
	c4= len(re.findall(r'\w+',s4))
	c5= len(re.findall(r'\w+',s5))
	c6= len(re.findall(r'\w+',s6))
	c7= len(re.findall(r'\w+',s7))
	mylist=[] #create an empty list
	mylist.append(c1) #insert the number of words of the first sentence.
	mylist.extend((c2,c3,c4,c5,c6,c7)) # insert the number of words of  the following sentences
	newlist=[]
	[newlist.append(x) for x in mylist if x not in newlist]
	newlist.sort(key=int, reverse=True) #sort the list with greatest number first
	
	print("The longest sentence is this text contains ", newlist[0], "words")
	print("The second longest sentence is this text contains ", newlist[1], "words")
	print("The third longest sentence is this text contains ", newlist[2], "words")
	print("The fourth longest sentence is this text contains ", newlist[3], "words")
	print("The shortest sentence is this text contains ", newlist[4], "words")

characters=0
lekseis=0


def countCharacters():
    #num_chars= len(re.findall('\S',text))    
    #print("Second way: ",num_chars)
    
    nodots= re.sub(r'[.,]', "", text) #I remove all dots and commas from the text

    numList = []
    output=[] #an empty list to insert all the words without duplications

    lekseis = nodots.split() #here I create a list with the words of the text
    for x in lekseis:  # a loop to remove all duplicate words from the text
    	if x not in output:
    		output.append(x)

    for i in output:
    	numList.append(len(re.findall('\S',i))) #count of the number of characters for each word
    #print(numList)    
    #print(output)

    #print (nlargest(5, numList))

    max_index=heapq.nlargest(5, range(len(numList)), numList.__getitem__) #a variable to store the indexes of the five longest words
    #print(max_index)

    
    for i in max_index:
	    print("The five longest words are: ",output[i])	#I compare the indexes of the two lists. Max_index
	                                                    #contains numbers which corresponds to the number
	                                                    # of characters and output contains the words 

countSentences() #call of the function countSentences
countWords()     #call of the function countWord
countWordsinSentences()
countCharacters()