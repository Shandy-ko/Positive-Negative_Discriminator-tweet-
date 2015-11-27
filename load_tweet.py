import tweepy
from datetime import timedelta

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

timelines =[]
for page in tweepy.Cursor(api.user_timeline,screen_name="").pages(#number):
    timelines.extend(page)

dates = []
tweets = []
for timeline in timelines:
    dates.append(timeline.created_at+timedelta(hours=9))
    tweets.append(timeline.text.encode('utf-8'))
    print timeline.created_at+timedelta(hours=9)
    print timeline.text.encode('utf-8')
