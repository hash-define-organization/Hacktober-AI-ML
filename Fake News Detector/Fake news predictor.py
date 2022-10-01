# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dvnUaTRFKuI5z9Ml48fxE-kU1Dh910vb
"""

from google.colab import files
uploaded = files.upload()

import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')

print(stopwords.words('english'))

import io
news_dataset = pd.read_csv(io.BytesIO(uploaded['fake news data set.csv']))

news_dataset.head()

news_dataset.isnull().sum()

news_dataset = news_dataset.fillna('')

news_dataset['content'] = news_dataset['author']+''+ news_dataset['title']

X = news_dataset.drop(columns='label', axis=1)
Y = news_dataset['label']

port_stem = PorterStemmer()

news_dataset['content'] = news_dataset['content'].apply(stemming)

print(news_dataset['content'])

X = news_dataset['content'].values
Y = news_dataset['label'].values

print(X)

print(Y)

Y.shape

vectorizer = TfidfVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)

print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)

model = LogisticRegression()

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)

X_new = X_test[3]

prediction = model.predict(X_new)
print(prediction)

if (prediction[0]==0):
  print('The news is Real')
else:
  print('The news is Fake')