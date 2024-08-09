import cv2
from ultralytics import YOLO
import time
import sys

sleep_time=float(sys.argv[1])
model_sample_model = YOLO("./models/sample_model/yolov8n.pt", task="detect")

#for _ in range(1000):
image = cv2.imread("026-dvd2_star_wars_poster_classic_1_web.jpg")
image = cv2.resize(image, (640, 640))
while True:
    print(f'RUN  -----------------------------------------------------------------')
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
    time.sleep(sleep_time)
