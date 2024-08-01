import requests
import time
import pickle
import ultralytics
from ultralytics import YOLO
import cv2
print('Start')

image = cv2.imread("/tmp/test.jpg")
image = cv2.resize(image, (640, 640))
model = YOLO("grpc://localhost:8001/yolo_onnx/v2/models/yolov8/infer", task="detect")

for i in range(1,5):
    print(f'RUN {i} ------------------------------------------------------')
    start = time.time_ns()
    # Load the Triton Server model
    tracks = model.track(
        image,
        conf=0.6,
        persist=True,
        tracker="bytetrack.yaml",
        show=False,
        verbose=True,
    )

    end = time.time_ns()
    print(f'Start: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')

    ## Print results
    boxes = tracks[0].boxes.xyxy.cpu()
    clss = tracks[0].boxes.cls.cpu().tolist()
    track_ids = tracks[0].boxes.id.int().cpu().tolist()
    for box, track_id, cls in zip(boxes, track_ids, clss):
        print(f'Track: {track_id}, Class:{cls}, Box:{box}')

