import tweepy as tw
import pandas as pd
import requests
import json
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
access_token = "1126320149202472963-WFvSDnYa1eL6osrEorVskuxFLAsoZB"
access_token_secret = "tYUy2yIjqPGtBYPxVUGwNl71rnFqErsMXCM05nAFphvUf"
consumer_key = "svHJE3Vx9Yo6IIxGRoCtZwkK5"
consumer_secret = "pmMPOP6ccTWxl675HCprsTyKnyQzWK6Vz9ZupnBSTp2uehVH73"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#khaleesi"
date_since = "2019-05-01"


tweets = tw.Cursor(api.search,
            q=search_words,
            lang="en",
            since=date_since, encode="utf-8").items(1000)
tweets_list = []
for tweet in tweets:
   #print(tweet)
   tweets_list.append(tweet.text)
#    tweets_list.append(tweet.created_at)
   #response = requests.get(tweet).json()
   #print(response)
tweet_df = pd.DataFrame({
   "Text": tweets_list
})