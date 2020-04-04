from application import *
from apikeys import *
import tweepy

interested_keyword = "#CoronaVirus"

# Average for every 10 tweets processed
average_time_step = 10
listener = Listener(interested_keyword, average_time_step)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

stream = Streamer(auth, listener, interested_keyword)

def stream_multiple(interested_keywords):
    ## TODO: use threading to stream multiple keywords at once and compare
    pass

if __name__=='__main__':
    stream.start_stream()
    if sys.response() == "Stop":
        print("Stop")
