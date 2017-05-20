import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth() :

	try :
		c_key = os.environ['TWITTER_CONSUMER_KEY']
		c_secret = os.environ['TWITTER_CONSUMER_SECRET']
		a_token = os.environ['TWITTER_ACCESS_TOKEN']
		a_secret = os.environ['TWITTER_ACCESS_SECRET']
	except KeyError:
		sys.stderr.write("twitter_* environment vars not set\n")
		sys.exit(1)

	auth = OAuthHandler(c_key, c_secret)
	auth.set_access_token(a_token, a_secret)
	return auth

def get_twitter_client() : 
	auth = get_twitter_auth()
	client = API(auth)
	return client
