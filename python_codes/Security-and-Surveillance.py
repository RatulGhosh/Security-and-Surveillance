
# coding: utf-8

# In[ ]:

from tempimage import TempImage
from dropbox.client import DropboxOAuth2FlowNoRedirect
from dropbox.client import DropboxClient
import argparse
import warnings
import datetime
import imutils
import json
import time
import cv2

warnings.filterwarnings("ignore")
client = None
flow = DropboxOAuth2FlowNoRedirect('nr0jeaiosy9hxz3','wr7zru0rejnluu3')
print "[INFO] Authorize this application: {}".format(flow.start())
authCode = raw_input("Enter auth code here: ").strip()

(accessToken, userID) = flow.finish(authCode)
client = DropboxClient(accessToken)
print "[SUCCESS] dropbox account linked"
camera = cv2.VideoCapture(0)
time.sleep(0.25)

# initialize the first frame in the video stream
firstFrame = None
avg = None
lastUploaded = datetime.datetime.now()
motionCounter = 0
# loop over the frames of the video
while True:
    # grab the current frame and initialize the occupied/unoccupied
    (grabbed, frame) = camera.read()
    timestamp = datetime.datetime.now()
    text = "Unoccupied"
 
    # end of video

    if not grabbed:
        break
 
    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    #cv2.imshow("Security Feed", frame)
 
    # if the first frame is None, initialize it
    if avg is None:
        print "[INFO] starting background model..."
        avg = gray.copy().astype("float")
        continue
    
    # compute the difference between the current and initial frame
    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    
    # threshold the delta image
    thresh = cv2.threshold(frameDelta, 25, 255,
        cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    (_ ,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
 
    # find contours on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    (_ ,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
 
    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < 200:
            continue
 
        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
        
        #get request to node_mcu
        requests.get('http://192.168.43.201/gpio/1')
        time.sleep(0.5)
        requests.get('http://192.168.43.201/gpio/0')
        
        # draw the text and timestamp on the frame
        cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
        0.35, (0, 0, 255), 1)
 
   # check to see if the room is occupied
    if text == "Occupied":
        # check to see if enough time has passed between uploads
        if (timestamp - lastUploaded).seconds >= 3:
            # increment the motion counter
            motionCounter += 1
 
            # check to see if the number of frames with consistent motion is
            # high enough
            if motionCounter >= 3:
                # check to see if dropbox sohuld be used
                if True:
                    # write the image to temporary file
                    t = TempImage()
                    cv2.imwrite(t.path, frame)
 
                    # upload the image to Dropbox 
                    print "[UPLOAD] {}".format(ts)
                    path = "{base_path}/{timestamp}.jpg".format(
                        base_path="python", timestamp=ts)
                    client.put_file(path, open(t.path, "rb"))
                    t.cleanup()
 
                # update the last uploaded timestamp and reset the motion
                # counter
                lastUploaded = timestamp
                motionCounter = 0
 
    # otherwise, the room is not occupied
    else:
        motionCounter = 0
    # display the security feed
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

