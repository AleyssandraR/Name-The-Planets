import cv2

solarSystem=cv2.imread('solar-System.jpg')
cv2.putText(solarSystem, 'The Sun', (75,50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Mercury', (115,250), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Venus', (190,170), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Earth', (290,270), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Mars', (390,170), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Jupiter', (570,380), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Saturn', (780,120), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Uranus', (970,290), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.putText(solarSystem, 'Neptune', (1110,140), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(225,225,225))
cv2.imshow('The Solar System', solarSystem)
cv2.waitKey(0)