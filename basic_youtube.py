# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:20:44 2020

@author: user
"""

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=9c-bTpPDu34')

yt.title
yt.streams.all()
yt.streams.filter(resolution="1080p").all()
yt.streams.filter(res="1080p").all()[0]
yt.streams.filter(res="1080p").first()
yt.streams.filter(res="1080p",video_codec="vp9").all()
yt.streams.filter(res="1080p",subtype="webm").all()

stream = yt.streams.filter(res="1080p").first()
stream.download('./videos')