from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "114010579-UscavtyluJ4ZOjGBGPwF3Xy8i5ynDgmeiYRLQ9WL"
access_token_secret = "hnA5I14kCwovdQF1Ciyz3VWOJlPlre8jHEKoeb9OshhJe"
consumer_key = "j2BhP2Q3LFCzpPQ5o0Xx4GuY7"
consumer_secret = "vkcmHL1U71cpqdn1LBl7GY4cdJIkvFotKAyZeChIuHBoq5aQ2j"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Game of Thrones', 'A Song of Ice and Fire', 'Iron Throne'])