# Imports
# -*- coding: utf-8 -*-
import nltk
# nltk.download()#If needed download required nltk text

'''
NLTK is an incredibly useful python package for doing many basic text manipulations.
Like many packages, NLTK has its own object that enables much of its functionality.
'''

'''
First, create a NLTK text object by importing a text file or importing from NLTK corpus
'''
def createNLTKObject(txtFile):
    f=open(txtFile,'rU')
    raw=f.read()
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    return text
from nltk.book import text3 #imports The Book of Genesis

'''
To get the context of a word or a dispersion plot
'''
text3.concordance("God") #this shows every occurrence with some context
text3.similar("God") #shows other words that appear in a similar context
text3.dispersion_plot(["God","Adam","Noah","Abraham","Joseph"])
# print(len(text3))

#shows and lists the vocabulary (unique) in text3.  Sorted puts capitalized words first.
# vocabSize=sorted(set(text3)) 

'''
Lexical diversity is how many times, on average, a word is used in the entire text
'''
def lexicalDiversity(text): #this function shows how many times on average a word is used
    return len(text)/len(set(text)) #larger results mean less diversity, lower is high diversity

# print(lexicalDiversity(text3))

'''
Frequency distributions show the tallies of each word used
'''
from nltk.probability import FreqDist
fdist=FreqDist(text3) #this gives the frequency distribution of every word. i.e. tallies of each word used
vocab = fdist.items() #list/dict of words from freq dist with keys and values
# print(vocab)
# hapaxes=fdist.hapaxes() #hapaxes are words that only appear once
# fdist.plot(25) #plot 25 most common tokens
# fdist.tabulate()

#now we can try to filter out and only get important words of a critical length and occurrence
uniqueWord = set(text3)
importantWords = [wd for wd in uniqueWord if len(wd)>5 and fdist[wd]>10] 
# print(sorted(importantWords))

#Collocations - show words that appear together most often
c=text3.collocations()
# print(c)

#Extract num chars, words and sents
numChar=0
numSents=0
for ind in text3:
    numChar = numChar+len(ind)
    #import os
    #os.system("say '{}'".format(ind))
    if ind==".":
        numSents=numSents+1
numWords=len(text3)
avgWordLen = numChar/numWords
wordsPerSent = numWords/numSents
# print("There are {} total words.  The average word length is {} and there are {} words per sentence on average.".format(
#     numWords,avgWordLen,wordsPerSent))

'''
Sentiment analysis using open source packages: Textblob, Polyglot, and NLTK
'''

def sentimentTB(sentence):
    from textblob.blob import TextBlob
    sentBlob = TextBlob(sentence)
    sentiment = sentBlob.sentiment.polarity
    return sentiment

def sentimentPG(object):
    from polyglot.text import Text
    text = Text(object)
    try:
        out = text.polarity
    except ZeroDivisionError:
        out = 0
    return out
    
def sentimentNL(object):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(object)
    return (-1*sentiment['neg'])+sentiment['pos']


