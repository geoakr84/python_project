import re
import string
import itertools

f1 = open("Muller1861_lecture1.txt", encoding='utf-8')
f2 = open("Sapir1921_chapter1.txt", encoding='utf-8')
f3 = open('stopwordlist.txt','r', encoding='utf-16').read()

text1 = f1.read()
text2 = f2.read()

inew=text1.replace("\n","") #removal of newlines from the text
inew2=re.sub(r'^.*\\When','When',inew) #remove everything from the beginning of the text until the first word "When"
inew3=inew2.replace("\\"," ") #replace \ with space
inew4=re.sub(r'[\']9[0-9](?=if|he|it|nay|by|and|the|as|At|Life|Nations|a|not|'')','',inew3) #regular expression to remove unwanted encoding from the text
inew5=re.sub(r'[ \']92s','\'s',inew4)
inew6=re.sub(r'God \'s','God\'s',inew5)
words=["uc0","u8208","u275", "'e2dh", "'e2"]
for w in words:
	if w in inew6:
		inew6=inew6.replace(w,"")
inew7=re.sub(r' +',' ',inew6)
underscore=re.findall('_\w+_',inew7) #regular expression to find specific words that start with _ and end with _
for i in range(len(underscore)):
	if underscore[i] in inew7:
	    inew8=re.sub(r'_','',inew7) # delete the _

f1sen = inew8.split('.') # create a list of strings where every string represents a sentence

jnew=text2.replace("\n","")
jnew2=re.sub(r'^.*\\Speech','Speech',jnew)
jnew3=jnew2.replace("\\"," ")

f2sen=[]
f2sen = jnew3.split('.') 

firstlist=[]
nodots= re.sub(r'[.,()-;\']', "", inew8) #remove dots and commas from the text
firstlist=nodots.split()
firstlist2=[]
for i in firstlist:
	firstlist2.append(i.lower())
firstlist3=[]
firstlist4=[]

secondlist=[]
nodots2= re.sub(r'[.,()-;\']', "", jnew3) #remove dots and commas from the text
secondlist=nodots2.split()
secondlist2=[]
for i in secondlist:
	secondlist2.append(i.lower())
secondlist3=[]
secondlist4=[]

thirdlist=[]
thirdlist=f3.split()

header = ("Length, Sentence, Chapter, Ranking")


chapter1=(1,) #creation of a tuple item for the column chapter
chapter2=(2,)
ilist1=[]
ilist2=[]
ilist3=[]
ilist4=[]
jlist1=[]
jlist2=[]
jlist3=[]
jlist4=[]
finallist=[]
final=[]

def countWords():	  	
	for i in f1sen:  
		ilist1.append(i)
		ilist2.append(len(re.findall(r'\w+', i)))  	

	for j in f2sen:
		jlist1.append(j)
		jlist2.append(len(re.findall(r'\w+', j)))  #command to count all the words    


	 
	ilist3=tuple(zip(ilist2,ilist1)) #for the items of this list I append the column chapter 2
	for x in ilist3:
		x=x+chapter2
		ilist4.append(x)	   
	i1=sorted(ilist4, key=lambda tup: (tup[0]), reverse=True)
	i2=i1[:10]
	#print(i2)

	jlist3=tuple(zip(jlist2,jlist1)) #for the items of this list I append the column chapter 1
	for x in jlist3:
		x=x+chapter1
		jlist4.append(x)
	t1=sorted(jlist4, key=lambda tup: (tup[0]), reverse=True)
	t2=t1[:10]
	#print(t2)

	finallist=ilist4+jlist4 # merge the two lists
	f1=sorted(finallist, key=lambda tup: (tup[0]), reverse=True)
	f2=f1[:10]
	
	for i in f2:
		final.append(list(i))
	
	counter=1
	
	for c in final:  #in this I create the column ranking with the use of an increment
		c.insert(3,counter)
		counter=counter +1
	
	header="Length. Sentence. Chapter. Ranking"
	data=""

	data='\n'.join('.'.join(map(str, row)) for row in final) #command to convert the list of lists in a string
	
    
	
	csvString=header +"\n" +data
	#print(csvString)

	fw = open("myData.csv", "w+")
	fw.write(csvString)
	print("File stored")

def findMostUsedWords():

	for i in firstlist2: #removal of the stop words
		if i not in thirdlist:
			firstlist3.append(i)
	

	wordcounter={}
	wordcounter2={}
	charlen1=0
	charlen2=0
	ch2=2
	ch1=1
	header="Keyword" + "," + "Frequency" + "," + "Length" + "," + "Chapter"
	dedomena= ""

	for x in firstlist3:
		if x in wordcounter:
			wordcounter[x] += 1
		else:
			wordcounter[x] = 1
	s= [(k, wordcounter[k]) for k in sorted(wordcounter, key=wordcounter.get, reverse=True)]

	s2= s[:10] # select the ten first words of the list
	for w in s2:
		firstlist4.append(list(w))

	for i in firstlist4:
		charlen1=len(re.findall('\S',i[0]))
		i.insert(2,charlen1)
		i.insert(3,ch2)
	


	for w in secondlist2:  #removal of the stop words
		if w not in thirdlist:
			secondlist3.append(w)

	for y in secondlist3: 
		if y in wordcounter2:
			wordcounter2[y] += 1
		else:
			wordcounter2[y] = 1
	p= [(q, wordcounter2[q]) for q in sorted(wordcounter2, key=wordcounter2.get, reverse=True)]

	p2= p[:10] # select the ten first words of the list
	for w in p2:
		secondlist4.append(list(w))

	for i in secondlist4:
		charlen2=len(re.findall('\S',i[0]))
		i.insert(2,charlen2)
		i.insert(3,ch1)
	
	
	unitedlist=[]
	unitedlist2=[]
	unitedlist=firstlist4 + secondlist4 #united list contains 10 + 10 most used words from each book

	unitedlist2 = sorted(unitedlist, key=lambda x: x[1], reverse=True)

	dedomena = '\n'.join(','.join(map(str, row)) for row in unitedlist2) #command to convert a list of list into a string

	csvString2 = header + "\n" + dedomena
	
	fw2 = open("myData2.csv", "w+")
	fw2.write(csvString2)
	print("File2 stored")



	





findMostUsedWords()
countWords()



