# Summary
Inspired by the COVID-19 epidemic, I decided I wanted to know more about the sentiment of tweets surrounding #CoronaVirus, #DonaldTrump's
response and any news around #AnimalCrossing. So, I built this application based off of a coding challenge that I had done a few months
back.

## Example Images 
These are some images after implementing plotting and averaging of the scores. I weighted negative scores .3 times higher than positive ones because it seemed like positive scores dominated the negative ones from before; which makes sense - people probably don't want to be on social media ripping into certain things besides a vocal minority, in which they really rip into something. 

![Application run on CoronaVirus](https://github.com/JimmyMinhLee/TweetSentimentAnalysis/blob/master/%23CoronaVirus04042020.png)
![Application run on DonaldTrump](https://github.com/JimmyMinhLee/TweetSentimentAnalysis/blob/master/%23DonaldTrump04042020.png)
![Application run on AnimalCrossing](https://github.com/JimmyMinhLee/TweetSentimentAnalysis/blob/master/%23AnimalCrossing04042020.png)


## How does it work?
I used the tweepy and vaderSentimentAnalysis libraries to handle all of the work. I had to make a custom Listener class and implement a
custom way to process the data, but a lot of the heavy lifting is handled by those libraries - which may be why the results are a little poor
as of right now. Running the app.py file will livestream the tweets and give you a rough composite score of the the provided hashtag's sentiment is.

## My plans for the future
I list out some methods with to-do bodies that I plan on implementing in the future. The goal is to connect this Python application to a working front
end so that anyone who's interested in public perception of a specific topic can use it to see the data in real time. It might also be
in my best interest to log these results in some database somewhere, but I think I'll do that when I learn more about databases!

EDIT (April 4th, 2020): Implemented a basic averaging setup - I just average every ten tweets that I process; and also used pyplot to plot the overall score and the individual scores being processed. Next, I want to figure out how to plot an average line and figure out some way to better clean the data, because as of right now, all tweets seem to be getting happier and happier about CoronaVirus. I'm thinking about maybe weighting negative scores more, but we'll have to see.
