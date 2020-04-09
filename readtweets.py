import tweepy as tw
def readtweets(searchterm,tw_key1,tw_key2):
    auth = tw.OAuthHandler('kf4P8Edo8ZXtvgZU8RsmsqY1L', '3nyDtxBbeXrJLxo9u5fC8yXbkSySxJTGTSEz26tDc06nAWSm6s')
    api = tw.API(auth, wait_on_rate_limit=True)
    termlength=len(searchterm)
    tweetlist=[]
    if searchterm[0] == '@':
        sn=searchterm[1:termlength]
        for tweets in api.user_timeline(screen_name=sn, result_type = 'recent', tweet_mode = 'extended', count = 200):
            tweetlist.append(tweets.full_text)
    else:
	# used https://stackoverflow.com/questions/14856526/parsing-twitter-json-object-in-python to figure out how to pull ONLY the text from the file
	# leveraged https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets for how to exclude retweets from twitter list and eliminate duplicates
        for tweets in api.search(q=searchterm, lang = 'en', result_type = 'recent', count = 200):
            if not tweets.retweeted and 'RT @' not in tweets.text:
                tweetlist.append(tweets.text) 
    return tweetlist