from random import *
import requests
import json

#id de playlist
robin = "PL_6o6_PExLl5Z8eUoDTEBoVrMAusrWikN&key=AIzaSyAg2WMM9qyYMLOCvG3TqPbJ9dgbmlFE6zs"
hayate = ""
suleyman = ""

def start(name):
	url = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId="
	if (name == "robin"): url += robin
	if (name == "hayate"): url += hayate
	if (name == "suleyman"): url += suleyman
	response = requests.get(url)
	jj = json.loads(response.text)
	return findUrl(jj['items'])

def findUrl(items):
	index = randint(0, len(items) - 1)
	chosen = items[index]['contentDetails']['videoId']
	return "https://www.youtube.com/watch?v=" + chosen



