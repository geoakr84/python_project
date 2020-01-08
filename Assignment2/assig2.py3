import re
import string
from  collections import Counter
from operator import itemgetter
import itertools

str = open('chapter1.txt', 'r').read() #command to open the text inside a variable
str=str.replace('INTRODUCTORY: LANGUAGE DEFINED','') #I erase the title because I don't need it
str=str.replace('\n',' ')  #command to erase all \n from the text


file = open('stopwordlist.txt','r').read()

count = len(re.findall(r'\.', str))  #\. count all dots to calculate how many sentences the text has 

	    
numberlist=[]
textlist=[]
sentences=str.split('.') #create a list of strings with all the sentences. I use the dot as a separator
print("Task 2-----------------------")
def findlongest():
	for line in sentences:
	    numberlist.append(line.rstrip('\n')) #command to erase all \n from the text


	count =0
	maxword = 0


	for word in numberlist:
		count= len(re.findall(r'\w+', word)) #command to count all the words
		textlist.append(count)	
    
	for i,j in enumerate(textlist):
		maxword=max(textlist) #this value contains the max number of words        
		if (j==maxword):            
			print("The longest sentence has ",maxword,"words and is the following one: ",numberlist[i])


def findlongestWord():
    wordlist=[] #create an empry list
    wordcount=0
    
    nodots= re.sub(r'[.,]', "", str) #remove dots and commas from the text
    nodots2= re.sub(r'[-]', " ", nodots) # replace - with space
    wordcount=nodots2.split()  # add to the empty list a list of strings which represent all the words of the text   
    
        
    for i in wordcount:        
        wordlist.append(len(re.findall('\S',i)))

    index=wordlist.index(max(wordlist)) # find the position inside the list of the word with maximum length of characters
    print("Task 3-----------------------")
    print("The longest word is: ",wordcount[index]) # print the word



wordscount=0
mainlist=[]
lowerlist=[]

def findTop():	    
    newlist=file.split() #create a list of strings with the removed words file
    newlist.pop(0) # because the first word (a) does not appear as wanted I remove it
    newlist.insert(0,"a") # and insert it here properly
    
    nodots= re.sub(r'[.,"();]', "", str) # remove .,"(); from the text
    nodots2= re.sub(r'[-]', " ", nodots) # replace - with space
    wordscount=nodots2.split()

    for j in wordscount:
    	lowerlist.append(j.lower())  # create a new list with all words in lower characters  

    for w in lowerlist:
    	if w not in newlist: # if the word is not in the removed words add it to the list mainlist
    		mainlist.append(w)
    
    
    word_counter={} 
    for word in mainlist: 
    	if word in word_counter: #if the word is in the mainlist
    		word_counter[word] += 1 #increment every time you find it
    	else:
    	    word_counter[word] = 1
    s= [(k, word_counter[k]) for k in sorted(word_counter, key=word_counter.get, reverse=True)] #sort the list from maximum to minimum
    
    s2=s[:10] # put in the variable the first ten words that have the most occurrences
    print("Task 4-----------------------")
    print("The top 10 most used words are: ",s2)	   

protaseis= str.split('.')
mainL=[]
finalL=[] 
uniqueL=[]
capitalL=[]
capitalL2=[]
capitalL3=[]
first=[]
second=[]
def named_entities():
    newlist=file.split() #create a list of strings with the removed words file
    newlist.pop(0) # because the first word (a) does not appear as wanted I remove it
    newlist.insert(0,"a") # and insert it here properly
    
    for w in range(len(protaseis)):       
           s=re.sub(r'^\W*\w+\W*', '',protaseis[w]) #command to erase the first word of the sentence           
           s.split()
           mainL.append(s) 
    
    
    for st in range(len(mainL)):
        u=mainL[st].split()
        finalL.append(u)
    

    mergedL= list(itertools.chain(*finalL)) #command to merge the lists in mainL into one big list of strings

    for x in mergedL:
        if x not in newlist:
            uniqueL.append(x)
    
    for x in uniqueL:
        if x[0].isupper():
            capitalL.append(x)

    for i in capitalL:
        nodots= re.sub(r'[.,"();]', "", i)
        capitalL2.append(nodots)

    for j in capitalL2:
        if j not in capitalL3:
            capitalL3.append(j)

    for ch in capitalL3:
        if re.match(r'^[A-L]',ch): #regular expression to check if the first character starts with A-L
            first.append(ch)
        else:
            second.append(ch)
    print("Task 5-------------------------------")
    print("This is the first list: ",first)
    print("This is the second list: ",second)


findlongest()
findlongestWord()
findTop()
named_entities()
    
    
        



