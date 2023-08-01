import pandas as pd
import urllib.request
import cv2
import numpy as np

def url_to_image(url):
    try:
        resp = urllib.request.urlopen(url)
        img = np.asarray(bytearray(resp.read()), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        return img
    except urllib.error.HTTPError as e:
        return None

# Assuming tha we have a DataFrame named 'df_3' with a 'Poster' column containing image URLs

image_arrays = []
counter = 0

# Running the loop for only 10 images
for i, link in enumerate(df_3['Poster']):
    if counter >= 10:
        break
    try:
        img_array = url_to_image(link)
        if img_array is not None:
            image_arrays.append(img_array)
            counter += 1
            print(f"Image {counter} extracted.")
    except Exception as e:
        print(f"Error in fetching the image from {link}. Error: {e}")
