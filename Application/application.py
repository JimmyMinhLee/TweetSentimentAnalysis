from utilities import *
import tweepy

class Streamer():
    def __init__(self, auth, listener, hashtag):
        self.hashtag = hashtag
        self.stream = tweepy.Stream(auth=auth, listener=Listener(hashtag))

    def start_stream(self):
        self.stream.filter(track=self.hashtag)

class Listener(tweepy.StreamListener):
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.processor = TextProcessor(self.hashtag)

    def on_data(self, raw_data):
        self.process_data(raw_data)

    def hashtags(self):
        return self.hashtag

    def process_data(self, raw_data):
        self.processor.process(raw_data)

    def on_error(self, error_code):
        if error_code == 420: return False
