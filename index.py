import detect
import gtts
import playlist
from playsound import playsound
import sys
import cv2
from random import *
import pygame
import pafy
import vlc
import greetings

def main():
	name = detect.start()
	print(name)
	profile = initProfile(name)
	greet(profile["greet"])
	playoxx = playMusic(profile["song"])
	looop(playoxx)

def looop(playoxx):
	while True:
		q = input()
		if (q == "q"):
			quitApp(playoxx)
		if (q == "r"):
			reset(playoxx)


def greet(sentence):
	tts = gtts.gTTS(sentence, lang="fr")
	tts.save("data/sounds/w.mp3")
	playsound("data/sounds/w.mp3")

def playMusic(url): #stream depuis url yt 
	video = pafy.new(url)
	best = video.getbestaudio()
	playurl = best.url

	Instance = vlc.Instance()
	player = Instance.media_player_new()
	Media = Instance.media_new(playurl)
	Media.get_mrl()
	player.set_media(Media)
	player.play()
	return player


def initProfile(name):
	profile = {
		"greet": greetings.start(name),
		"song": playlist.start(name)
	}
	return profile


def quitApp(p):
	p.stop()
	sys.exit()


def reset(p):
	p.stop()
	playsound("data/sounds/b.mp3")
	main()

main()