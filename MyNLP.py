# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:13:43 2017

@author: Raju garu
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import the dataset
dataset = pd.read_csv('E:\\Udemy MachineLearning\\Machine Learning A-Z Template Folder\\Part 7 - Natural Language Processing\\Section 36 - Natural Language Processing\\Natural_Language_Processing\\Restaurant_Reviews.tsv', delimiter = '\t',quoting =3)

#Clean the texts: removing stop words, apply stemming.
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus =[]
for i in range(1000):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ ps.stem(word) for word in review if  word not in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)



