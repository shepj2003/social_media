import sys
import os
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener

from twitter_client import get_twitter_auth

class CustomListener(StreamListener) : 
	
	def __init__(self, fname) : 
		dname = os.getenv('TWITTER_DATA_DIR', './')
		safe_fname = format_filename(fname)
		self.outfile = "%sstream_%s.json1" % (dname, safe_fname)

	def on_data(self, data) :
		try :
			with open(self.outfile, 'a') as f : 
				f.write(data)
				return True
		except BaseException as e :
			sys.stderr.write("Error on data {} \n".format(e))
			time.sleep(5)
		return True

	def on_error(self, status) : 
		if status==420 : 
			sys.stderr.write("rate limit exceeded\n")
			return False
		else: 
			sys.stderr.write("Error {} \n".format(status)) 
			return True

############################################################
## end of class CustomListener
############################################################
def format_filename(fname) : 
	return ''.join(convert_valid(one_char) for one_char in fname)

def convert_valid(one_char) :
	valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
	if one_char in valid_chars : 
		return one_char
	else : 
		return '_'

if __name__ == '__main__':
	query = sys.argv[1:]
	query_fname = ' '.join(query)
	auth = get_twitter_auth()
	twitter_stream = Stream(auth, CustomListener(query_fname))
	twitter_stream.filter(track = query, async = True)

