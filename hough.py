import cv2
import numpy as np
import sys

scale_percent = 60 # percent of original size

running = True

video = cv2.VideoCapture(1)

mode = "run"
udKey = "view"
rlKey = "scale"

modeMap = {
  "edge": {
    "thresholdMin": 180,
    "thresholdMax": 200,
    "apertureSize": 5
  }, 
  "hough": {
    "threshold": 100,
    "minLineLength": 100,
    "maxGapLength": 10
  },
  "run": {
    "view": 0,
    "scale": 60
  }
}

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (0,255,0)
lineType               = 2

while(running):
  frame = {}
  check, img = video.read(0)

  width = int(img.shape[1] * modeMap['run']['scale'] / 100)
  height = int(img.shape[0] * modeMap['run']['scale'] / 100)
  dim = (width, height)
  # resize image
  resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

  gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
  # Apply Canny edge detection, return will be a binary image
  edges = cv2.Canny(gray,modeMap['edge']['thresholdMin'],modeMap['edge']['thresholdMax'],apertureSize = modeMap['edge']['apertureSize'])
  # Apply Hough Line Transform, minimum length of line is 200 pixels
  lines = cv2.HoughLinesP(edges,1,np.pi/180,modeMap['hough']['threshold'],0,modeMap['hough']['minLineLength'],modeMap['hough']['maxGapLength'])

  views = [resized, gray, edges]
  view = views[modeMap['run']['view']]

  if lines is not None and len(lines) > 0:
    for line in lines:
      for x1,y1,x2,y2 in line:
          cv2.line(view,(x1,y1),(x2,y2),(0,255,0),2)

  cv2.putText(view,"mode: {0}".format(mode), 
      (10, 500), 
      font, 
      fontScale,
      fontColor,
      lineType)
  cv2.putText(view, "{0}: {1}".format(udKey, modeMap[mode][udKey]), 
      (10, 530), 
      font, 
      fontScale,
      fontColor,
      lineType)
  cv2.putText(view, "{0}: {1}".format(rlKey, modeMap[mode][rlKey]), 
      (10, 560), 
      font, 
      fontScale,
      fontColor,
      lineType)
  cv2.imshow("Line Detection", view)

  k = cv2.waitKey(1)
  if k == ord('q'):
    running = False
  elif k == ord('e'):
    mode = 'edge'
    udKey = 'thresholdMin'
    rlKey = 'thresholdMax'
  elif k == ord('h'):
    mode = 'hough'
    udKey = 'threshold'
    rlKey = 'minLineLength'
  elif k == ord('r'):
    mode = 'run'
    udKey = 'view'
    rlKey = 'scale'
  elif k==ord('w'):
    #up
    modeMap[mode][udKey] = modeMap[mode][udKey] + 1
  elif k==ord('s'):
    #down
    modeMap[mode][udKey] = modeMap[mode][udKey] - 1
  elif k==ord('d'):
    #right
    modeMap[mode][rlKey] = modeMap[mode][rlKey]+1
  elif k==ord('a'):
    #left
    modeMap[mode][rlKey] = modeMap[mode][rlKey]-1

cv2.destroyAllWindows()

