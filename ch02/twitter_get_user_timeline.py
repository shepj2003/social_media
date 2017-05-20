import json
import sys
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
	user = sys.argv[1]
	client = get_twitter_client()
	dname = '/home/shepj/data/'
	fname = "user_timeline_{}.json".format(user)

	with open (dname + fname,'w') as f:
		for page in Cursor(client.user_timeline, screen_name=user, count = 200).pages(16):
			for status in page:
				f.write(json.dumps(status._json, indent = 4) + "\n")
