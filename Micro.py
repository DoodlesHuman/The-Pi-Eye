# Object Detection and Caption Reading

import requests
from time import sleep
from picamera import PiCamera
import os
from gtts import gTTS

# Step 1: Capture image
camera = PiCamera()
camera.resolution = (1280, 720)
sleep(1)
camera.capture('2.jpg')
camera.close()

# Step 2: Call Microsoft Computer Vision API
subscription_key = "" # Provide Azure key
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"

image_data = open("2.jpg", "rb").read()
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}
params = {'visualFeatures': 'Categories,Description,Color'}

response = requests.post(vision_analyze_url, headers=headers, params=params, data=image_data)
analysis = response.json()
caption = analysis["description"]["captions"][0]["text"].capitalize()
print(caption)

# Step 3: Text to Speech
tts = gTTS(text=caption, lang='en')
tts.save("2.mp3")
os.system('mpg321 2.mp3')
