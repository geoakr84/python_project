import re
from itertools import chain

text = open("practice1.txt", encoding='utf-8').read()

c= re.findall('[A-Za-z0-9]+',text)
wordlist=[]
for w in c:
	wordlist.append(w.lower())

print(wordlist)
total=0
for c in wordlist:
	count=len(re.findall('\S',c))
	total= count + total
print(total)

list1=[]

for j in range (len(wordlist)):
	count2=len(re.findall('\S',wordlist[j]))
	list1.append(count2)


m=sorted(list1, reverse=True)
m2=[14,13,12]

list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
tup=()
for i,e in enumerate(list1):
	if e in m2:
		list2.append(i)


for x in list2:
	list3.append(wordlist[x])
print(list3)

for w in list3:
	if w not in list4:
		list4.append(w)

list4.sort(key=len, reverse=True)
list5=list4[:]

for ch in list5:
	count3=len(re.findall('\S',ch))
	list6.append(count3)

list7=list(chain(*zip(list5,list6)))
print(list7)

i=1
j="-"

for k in range(0,7):
	print("Word",i,"=",list5[k],"Number of characters: ",list6[k])	
	if (k==6):
		break
	if(list6[k] == list6[k+1]):
		i=i-1	
	i=i+1

def same_last(word1, word2):
	if (word1[-1:] == word2[-1:]):
		print("True")
	else:
		print("False")

def initials(argument):
	finalstr=[]
	init=argument.split(' ')
	for x in init:
		first=x[:1]
		finalstr.append(first)
	mystr=''.join(map(str,finalstr))
	print(mystr) 

def devowel(phrase):
	dw=re.sub(r'[aeuoiy]+','',phrase)
	print(dw)


same_last("power", "motor")
initials('Vladimir "Pootie-Poot" Putin')
devowel('George Akritidis')