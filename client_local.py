import numpy as np 
import base64
import zlib
import time
import cv2
import pickle
from ultralytics import YOLO
import pickle
import time


model_sample_model = YOLO("./models/sample_model/yolov8n.pt", task="detect")

#for _ in range(1000):
image = cv2.imread("test_image.jpg")
image = cv2.resize(image, (640, 640))
for i in range(1,5):
	print(f'RUN {i} -----------------------------------------------------------------')
	start = time.time_ns()
	tracks = model_sample_model.track(
	            image,
	            conf=0.5,
	            persist=True,
	            tracker="bytetrack.yaml",
	            show=False,
	            verbose=True,
	    )
	end = time.time_ns()
	print(f'Start: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')

