# Text Extraction and Speech

import os
from PIL import Image
from picamera import PiCamera
from time import sleep
import cv2
import imutils
import numpy as np
from ocrspace import ocrspace
from gtts import gTTS

# Step 1: Capture image
camera = PiCamera()
camera.resolution = (1280, 720)
camera.shutter_speed = 1500000
camera.iso = 1000
camera.brightness = 55
camera.contrast = 20
sleep(2)
camera.capture('f.jpg')
camera.close()

# Step 2: Rotate image
img = cv2.imread('f.jpg', 0)
rotated = imutils.rotate_bound(img, 270)
cv2.imwrite('10.jpg', rotated)

# Step 3: Enhance image
image = cv2.imread('10.jpg', 0)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
thresh = cv2.adaptiveThreshold(
    blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)
cv2.imwrite('9.jpg', thresh)

# Step 4: OCR
response = ocrspace('9.jpg', language='eng')
text_block = str(response)
start = text_block.find("ParsedText") + 12
end = text_block.find("FileParseExitCode") - 4
extracted = text_block[start:end]

if len(extracted) < 5:
    end = text_block.find("OCRExitCode") - 40
    extracted = text_block[start:end]

final_text = extracted.replace(r"\r\n", " ")
print(final_text)

# Step 5: Text to Speech
tts = gTTS(text=final_text, lang='en')
tts.save("2.mp3")
os.system('mpg321 2.mp3')
