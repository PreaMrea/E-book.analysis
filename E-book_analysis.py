import requests
from bs4 import BeautifulSoup as bs
def replace(words):
    words=words.replace("0"," ")   #we delete punctuation marks etc.
    words=words.replace("1"," ")
    words=words.replace("2"," ")
    words=words.replace("3"," ")
    words=words.replace("4"," ")
    words=words.replace("5"," ")
    words=words.replace("6"," ")
    words=words.replace("7"," ")
    words=words.replace("8"," ")
    words=words.replace("9"," ")
    words=words.replace("."," ")
    words=words.replace("="," ")
    words=words.replace(";"," ")
    words=words.replace(","," ")
    words=words.replace("_"," ")
    words=words.replace(")"," ")
    words=words.replace("("," ")
    words=words.replace("!"," ")
    words=words.replace("?"," ")
    words=words.replace("["," ")
    words=words.replace("]"," ")
    words=words.replace("<"," ")
    words=words.replace(">"," ")
    words=words.replace("/"," ")
    words=words.replace("#"," ")
    words=words.replace("'"," ")
    words=words.replace('"'," ")
    words=words.replace("*"," ")
    words=words.replace(":"," ")
    words=words.replace("-"," ")
    return words
def downloadbook(bookname):    # we download files
    book=bookname+".txt"
    url='https://en.wikibooks.org/wiki'
    bookname.replace("'",'%27')                             
    bookname.replace(' ','_')                             
    bookname='/'+bookname
    urlforbook=url+bookname+'/Print_version'
    file=open(book,'w', encoding='utf-8')
    Resource_Book=requests.get(urlforbook)
    soup =bs(Resource_Book.content, 'html.parser')
    for i in soup.find_all('div',attrs={'class':'mw-parser-output'}):
        content=i.text
        content=content
        words=content.lower().split(' ')
    for word in words:
        file.write(word+' ')
    file.close()    
def stopwordsclear(word):        # clear to stopwords
    stopwordsdirectory = 'stopwords.txt'
    STOP_WORDS = open(stopwordsdirectory,'r')
    stopwords=STOP_WORDS.read()  
    stopwords=stopwords.lower()
    stopwords = stopwords.split()
    STOP_WORDS.close()
    for a in stopwords:     #We take stopwords words
        for x in word:      #We check if book1 equals any element of words
            if(x==a):
                word.remove(x)
    return word
select=int(input("Do you want to look at 1 book or 2 books?"))
if(select==1):    
    bookname=input("Enter Book Name's : ")   #we get the file names from the user
    downloadbook(bookname)
    bookname=bookname+".txt"
    file1=open(bookname,'r',encoding='utf-8')   #read to file
    words=file1.read()
    file1.close()
    words=replace(words)
    words=words.split()
    words=stopwordsclear(words)
    wordscount=[]#her kelimeyi 1 kere içeri alıyoruz   
    wordscount.append([0,'']) 
    for i in words:
        wordscount.append([words.count(i),i])  
        for k in range(words.count(i)):
            words.remove(i) 
    wordscount.sort(reverse=True)
    print(" NO WORD","        ","FREQ_1")
    for x in range(20):
        print(x+1,"=>",wordscount[x][1],end="")
        b=15-len(wordscount[x][1])
        for i in range(b):
            print(" ",end="")
        print(wordscount[x][0])    
if(select==2):
    book1name=input("Enter first book name's:")
    book2name=input("Enter second book name's:")
     # Operations for first file (downland,read,replace,split,stopwords clear)  
    downloadbook(book1name)                 
    book1name=book1name+".txt"
    file1=open(book1name,'r',encoding='utf-8')
    words1=file1.read()
    file1.close()
    words1=replace(words1)
    words1copy=words1
    words1=words1.split()
    words1=stopwordsclear(words1)
    # Operations for second file (downland,read,replace,split,stopwords clear)
    downloadbook(book2name)                 
    book2name=book2name+".txt"
    file2=open(book2name,'r',encoding='utf-8')
    words2=file2.read()
    file2.close()
    words2=replace(words2)
    words2copy=words2
    words2=words2.split()
    words2=stopwordsclear(words2)
    print("1.Common Words")
    select1=int(input("2.Distinct words "))
    words1distinct=[]
    words1distinct.append([0,""])
    words2distinct=[]
    words2distinct.append([0,""])
    totalwords=words1copy+words2copy
    totalwords=totalwords.split()
    totalwords=stopwordsclear(totalwords)
    totalwordscommon=[]
    words1common=[]
    words2common=[]
    if(select1==1):
        for i in totalwords:
            totalwordscommon.append([totalwords.count(i),i])
            for k in range(totalwords.count(i)):
                totalwords.remove(i)
        for i in words1:
            words1common.append([words1.count(i),i])
            for k in range(words1.count(i)):
                words1.remove(i)

        for i in words2:
            words2common.append([words2.count(i),i])            
            for k in range(words2.count(i)):
                words2.remove(i)

        words1common.sort(reverse=True)    #we sort by word count
        words2common.sort(reverse=True)
        totalwordscommon.sort(reverse=True)
        print(" NO WORD","        ","FREQ_1","        ","FREQ_2","        ","FREQ_TOTAL","        ")     #design to screen
        for x in range(20):
            print(x+1,"=>",totalwordscommon[x][1],end="")
            b=15-len(totalwordscommon[x][1])
            for i in range(b):
                print(" ",end="")
            print(words1common[x][0],"           ",totalwordscommon[x][0]-words1common[x][0],"          ",totalwordscommon[x][0])
    elif(select1==2):
        print("1.First book distinc words ")
        select2=int(input("2.Second book distinc words?"))
        if(select2==1):            
            x=0            
            for i in words1:
                for k in words2:
                    if(i==k):
                        words1[x]="xxx"                        
                x=x+1
            for i in words1:
                if(i!="xxx"):
                    words1distinct.append([words1.count(i),i])  
                    for k in range(words1.count(i)):#we delete the word so that it does not check again after moving it
                        words1.remove(i)                                                               
            words1distinct.sort(reverse=True)
            for x in range(21):#How many of us are most frequently used are printed in descending order, if desired
                print(x+1,"=>",words1distinct[x][1],end="")
                b=15-len(words1distinct[x][1])
                for i in range(b):
                    print(" ",end="")
                print(words1distinct[x][0]) 
        elif(select2==2):
            x=0            
            for i in words2:
                for k in words1:
                    if(i==k):
                        words2[x]="xxx"                        
                x=x+1
            for i in words2:
                if(i!="xxx"):
                    words2distinct.append([words2.count(i),i])  
                    for k in range(words2.count(i)):#we delete the word so that it does not check again after moving it
                        words2.remove(i)                                                               
            words2distinct.sort(reverse=True)
            for x in range(21):#How many of us are most frequently used are printed in descending order, if desired
                print(x+1,"=>",words2distinct[x][1],end="")
                b=15-len(words2distinct[x][1])
                for i in range(b):
                    print(" ",end="")
                print(words2distinct[x][0]) 
if(select!=2 and select!=1):
    print("ERROR!! Please Select 1 or 2")
    quit()     
