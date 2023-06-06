import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import urllib.request
import cv2

df=pd.read_csv("MovieGenre.csv",encoding="latin1")
col=['Title','Year','IMDB Score','Genre']
df2=df[col]

def link_to_image(url):
    try:
        resp = urllib.request.urlopen(url)
        img = np.asarray(bytearray(resp.read()), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        return img
    except urllib.error.HTTPError as e:
        return None

image_arrays = []
counter = 0
for i, link in enumerate(df['Poster']):
    try:
        img_array = link_to_image(link)
        if img_array is not None:
            image_arrays.append(img_array)
            counter += 1
            print(f"Image {counter} extracted.")
        
        if counter >= 10:
            break
    except Exception as e:
        print(f"Failed to extract image from {link}.")
np.save("arrays_saved.npy",img_array)
