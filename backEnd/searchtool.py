import csv
import string
import numpy as np
import pandas as pd
import AutoChecker as ac
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# string.punctuation use to remove symbol (e.g. !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)
def remove_puncts(input_string, string):
    return str(input_string).translate(str.maketrans('', '', string.punctuation)).lower()
def searchByTitle(query):
    data = pd.read_csv('../Resources/Jikan_database.csv')
    title = data['title']
    corpus = title.to_numpy().tolist()
    cleaned_corpus = []
    for doc in corpus:
        cleaned_doc = remove_puncts(doc, string)
        cleaned_corpus.append(cleaned_doc)
    tokenized_clean_corpus = []
    # Ex. {[dragon ball]} -> {[dragon], [ball]}
    for doc in cleaned_corpus:
        doc = doc.split()
        tokenized_clean_corpus.append(doc)
    # print(tokenized_clean_corpus)
    # Create txt file
    # ac.trainTitleTextFile(ac.get_text(tokenized_clean_corpus))
    relevent_document = 0
    return ac.title_auto_correct(query)

def searchByDescription(query):
    data = pd.read_csv('../Resources/Jikan_database.csv')
    title = data['synopsis']
    corpus = title.to_numpy().tolist()
    cleaned_corpus = []
    for doc in corpus:
        cleaned_doc = remove_puncts(doc, string)
        cleaned_corpus.append(cleaned_doc)
    tokenized_clean_corpus = []
    for doc in cleaned_corpus:
        doc = doc.split()
        tokenized_clean_corpus.append(doc)
    # Create txt file
    # remove_dupe_stop_word = ac.get_text(tokenized_clean_corpus)
    # remove_dupe_stop_word = [word for word in remove_dupe_stop_word if not word in stopwords.words('english')]
    # ac.trainDescriptionTextFile(ac.get_text(remove_dupe_stop_word))
    return ac.description_auto_correct(query)