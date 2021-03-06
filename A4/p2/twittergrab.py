from __future__ import unicode_literals
import re 
import os
import sys
import json
import requests
import subprocess
from urlparse import parse_qs
from requests_oauthlib import OAuth1

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "bYGDX5XYHUrcadLKV3Q0pmtsh"
CONSUMER_SECRET = "sFuyxQ8mDHKmjgfAoavs4HqfGHuncTfSC9NdQjeF6gkiy4th8J"
OAUTH_TOKEN = "962384849293193217-Ab0Ag4PFmRZdaazcoG7OxhC7fa3QfOA"
OAUTH_TOKEN_SECRET = "6dSGlywYRVFalhJBMhxgt4n4z3jPcZq47Jnu3ZzILZHfo"

def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
		twitterUser = "acnwala"

		print 'Searching Twitter for followers counts of '+twitterUser+"'s followers: "
		oauth = get_oauth() 

		print '%-15s %-20s' %('Followers_count','Follower-screen-name')			
		
		# initial reading from the twitter account where cursor = -1 (e.g. first page)
		r = requests.get(url="https://api.twitter.com/1.1/followers/list.json?cursor=-1&count=2000&screen_name="+twitterUser+"&skip_status=true&include_user_entities=false", auth=oauth)
		counter = 0
		res = r.json()
		while True:
			raw_res = res['users']
			for init_url in raw_res:
				counter = counter + 1
				print '%-15d %-20s' %(init_url['followers_count'],init_url['screen_name'].encode('ascii', 'replace'))
				with open('twitter_counts.txt', 'a') as outfile:
				    outfile.write('%-15d\n' %(init_url['followers_count']))				
			if str(res['next_cursor']) == '0':
				break
			else:
				r = requests.get(url="https://api.twitter.com/1.1/followers/list.json?cursor="+str(res['next_cursor'])+"&count=100&screen_name="+twitterUser+"&skip_status=true&include_user_entities=false", auth=oauth)
				res = r.json()
	
print '\nNumber of '+twitterUser+"'s followers is: "+str(counter)