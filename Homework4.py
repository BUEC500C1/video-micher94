import os
import sys
from makeimage import makeimage
from readtweets import readtweets
from Queue import Queue
import configparser
import subprocess
from flask import Flask
app = Flask(__name__)


@app.route('/starthere/<keyword>')
def main(keyword):

	# get keys
	# config = configparser.ConfigParser()
	# config.read('C:/Users/micha/Documents/Spring2019/EC500/Homework4/keys')
	# print(config.get('auth','consumer_key').split())

	consumer_key = '8cRGDF5RPNboNrR8JaswNySuC'
	consumer_secret = 'BSX2gAzfqtHDw1cyELlapdomr96qy7Y1pn3D06koT8ZOixcpsu'
	access_token = '1172138619680673794-fGznWzLf465gsVed1SwI6kPPIqHikj'
	access_secret = 'TXb8K6iZ67MHoC03z5SgwBnmeOv3tajqbZqqd3QrT8CXb'

	q = Queue()

	inputlist = keyword
	inputlist = inputlist.split(',')

	for words in inputlist:
		q.queueup(words)

	q.queuelist()
	print(q.queuelength())

	i = 0
	filename = str(i) + "-%01d.png"
	videoname = keyword+".avi"
	while q.queuelength()>0:
		tweets = readtweets(q.items[0],consumer_key,consumer_secret)
		j = 0
		for tweet in tweets:
			print(tweet)
			makeimage(i,j,tweet)
			j=j+1
		q.queuedown()
		q.queuelist()
		i = i+1
		print("I am here")
		subprocess.call(['ffmpeg', '-framerate', '.1', '-i', filename, videoname])
	return keyword



if __name__ == '__main__':
    main()
