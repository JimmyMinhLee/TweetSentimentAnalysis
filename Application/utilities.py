import json, sys
from os import system
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class TextProcessor():
    def __init__(self, hashtag):
        self.name = hashtag
        self.hashtag = {hashtag:0}
        self.analyzer = SentimentIntensityAnalyzer()

    def process(self, raw_data):
        text = self.get_text(raw_data)
        response = self.analyzer.polarity_scores(text)['compound']
        self.hashtag[self.name] += response
        print(self.hashtag[self.name], text)

    def get_text(self, raw_data):
        try: return json.loads(raw_data)['text']
        except KeyError: return "KeyError encountered while streaming tweets."

    def plot(self, score):
        ## TODO: use matplotlib to plot the scores over time, maybe store in mysql somewhere
        pass 

    def normalize(self, response):
        ## TODO: find some way to normalize tweet scores
        pass

    def clean(self, text):
        ## TODO: may be useful to ignore certain tweets and use others, i.e rt
        pass
