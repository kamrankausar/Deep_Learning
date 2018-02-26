#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:14:27 2018

@author: kamran
"""

'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
#import numpy as np
import os

#CHange the Directory
os.chdir("/home/kamran/Deep Learning/Videos/Script")

# Playing video from file:
vid_cap = cv2.VideoCapture('trump.mp4')

# To get the frame rate of the Video
framerate = vid_cap.get(5)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
ret = True
vid_cap.set(cv2.CAP_PROP_POS_MSEC,20000)      # just capture to 20 sec. position
while(ret):
    # Capture frame-by-frame
    ret, frame = vid_cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    #print ('Creating...' + name)
    cv2.imwrite(name, frame)  # Saves the frame as an image

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
vid_cap.release()
cv2.destroyAllWindows()