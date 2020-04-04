import json, sys
from os import system
# from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

class TextProcessor():
    def __init__(self, hashtag):
        self.name = hashtag
        self.hashtag = {hashtag:0}
        self.analyzer = SentimentIntensityAnalyzer()

        # Averaging variables
        self.current_average = 0
        self.average_count = 0

        # Plotting variables
        self.total_step_count = 0
        self.x_data = [0]

        # Trend of sentiment vs. time
        self.trend_y_data = [0]
        # Individual y scores vs. time
        self.average_y_data = [0]

    def process(self, raw_data, average_step):
        text = self.get_text(raw_data)
        response = self.analyzer.polarity_scores(text)['compound']

        # Instantiate plot
        plt.ion()
        plt.ylabel('Average sentiment per 10 tweets')
        plt.xlabel('Tweet count processed')
        plt.plot(self.x_data, self.trend_y_data)
        plt.draw()

        # Perform averaging and plot
        self.normalize(response, average_step)

        # Perhaps putting into a method changes something about calculations? (It shouldn't?)
        # if self.average_count != average_step:
        #     self.current_average += response
        #     self.average_count += 1
        # else:
        #     self.hashtag[self.name] += self.current_average / self.average_count
        #
        #     # Append data
        #     self.total_step_count += 1
        #     self.x_data.append(self.total_step_count * 10)
        #     self.average_y_data.append(self.current_average / self.average_count)
        #     self.trend_y_data.append(self.hashtag[self.name])
        #
        #     # Reset
        #     self.current_average = 0
        #     self.average_count = 0
        #     self.plot()




    def get_text(self, raw_data):
        try: return json.loads(raw_data)['text']
        except KeyError: return "KeyError encountered while streaming tweets."

    def plot(self):
        # Update plot
        plt.plot(self.x_data, self.trend_y_data)
        plt.draw()
        plt.pause(0.1)

    def normalize(self, response, average_step):
        if self.average_count != average_step:
            self.current_average += response
            self.average_count += 1
        else:
            self.hashtag[self.name] += self.current_average / self.average_count

            # Append data
            self.total_step_count += 1
            self.x_data.append(self.total_step_count * 10)
            self.average_y_data.append(self.current_average / self.average_count)
            self.trend_y_data.append(self.hashtag[self.name])

            # Reset
            self.current_average = 0
            self.average_count = 0
            self.plot()

    def clean(self, text):
        ## TODO: may be useful to ignore certain tweets and use others, i.e rt
        pass
