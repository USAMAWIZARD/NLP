import numpy as np
import pandas as pd
import nltk
import tweepy
import csv
import json
url = r'https://raw.githubusercontent.com/annu1245/PantoMath/master/PantoMath/panto_math_app/static/datasets/tweets.csv'
df1 = pd.read_csv(url,  error_bad_lines=False)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    score.pop('compound', None)
    response = max(score, key=score.get)
    if response=='neg':
        return "negative"
    if response=='pos':
        return "positive"
    return "neutral"
df1.head()
tweets = set(df1['Tweets'])
print(len(tweets))
try:
    for tweet in tweets:
        sent=sentiment_analyzer_scores(tweet)
        row=[tweet,sent ]
        with open(r'tweetslabeleddata.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

except:
    print(tweet)
    pass