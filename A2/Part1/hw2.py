#!/usr/bin/env python
from sets import Set
from ttp import ttp
from ttp import utils
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import unicodedata
import urllib
from urlparse import urlparse
from httplib import IncompleteRead


#config.py contains your twitter's API consumer_key, consumer_secret, access_key, and access_secret
#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = 'bYGDX5XYHUrcadLKV3Q0pmtsh'
csecret = 'sFuyxQ8mDHKmjgfAoavs4HqfGHuncTfSC9NdQjeF6gkiy4th8J'
atoken = '962384849293193217-Ab0Ag4PFmRZdaazcoG7OxhC7fa3QfOA'
asecret = '6dSGlywYRVFalhJBMhxgt4n4z3jPcZq47Jnu3ZzILZHfo'
unique_links = set()

class StdOutListener(StreamListener):
	def on_data(self, data):
		global unique_links
		# get the text from the tweet
		json_dict = json.loads(data)
		
		if 'text' not in json_dict:
			return True
		text = unicodedata.normalize('NFKD', json.loads(data)['text']).encode('ascii','ignore')
		parsed = ttp.Parser().parse(text)
		urls = parsed.urls
		# check if urls is empty and return immediately
		if not urls:
			return True

		# long_urls returns a dictionary of short_url to list[short_url, long_url]
		long_urls = utils.follow_shortlinks(urls)
		for url in urls:
			try:
			# use a regex to pull the link from the text
				links = long_urls[url]
				if links is not None:
				# long urls returns a dictionary with a list of each url - take the last one
					link = links[-1]
				# the link is real - now need to get the link address
					resp = urllib.urlopen(link)
					geturl = resp.geturl()
					parsedurl = urlparse(geturl)
					domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsedurl)
					if resp.getcode() == 200:		
					# add the long link to our unique links, or cancel if there's already 1000
						if len(unique_links) < 100:
							if link not in unique_links:
								if (domain != 'https://twitter.com/' and domain != 'https://t.co/'):
									f = open('url.txt','a')
									f.write(link +'\n')
									f.close()
									print link
									unique_links.add(link)
								else:
									return True
						
							return True
						else:
							return False
			except (IncompleteRead):
				pass


	def on_error(self, status):
		pass

if __name__ == '__main__':
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	stream_listener = StdOutListener()
	stream = Stream(auth, stream_listener)
	stream.filter(locations=[-180,-90,180,90], async=True)