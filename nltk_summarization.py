import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  
import bs4 as bs
import urllib.request
import re


def nltk_summarizer(raw_text):
	a=len(raw_text)
	# Removing Square Brackets and Extra Spaces
	raw_text = re.sub(r'\[[0-9]*\]', ' ', raw_text)
	raw_text = re.sub(r'\s+', ' ', raw_text)
	# Removing special characters and digits
	formatted_article_text = re.sub('[^a-zA-Z]', ' ', raw_text )
	formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

	sentence_list = nltk.sent_tokenize(raw_text)
	stopWords = set(stopwords.words("english"))
	word_frequencies = {}  
	for word in nltk.word_tokenize(formatted_article_text):  
	    if word not in stopWords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1

	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

	sentence_list = nltk.sent_tokenize(raw_text)
	sentence_scores = {}  
	for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]



	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)
	b=len(summary)
	sum=summary+"\n\n"+"Original length of text in chars is "+str(a)+'\n'+"Summary length of text in chars is "+str(b)

	return sum
	 
	