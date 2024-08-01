import numpy as np 
import base64
import zlib
from ultralytics import YOLO
import pickle
import time


model_sample_model = YOLO("./models/sample_model/yolov8n.pt", task="detect")

def predict(b64img_compressed, w, h):
    #start = time.time_ns()
    b64decoded = base64.b64decode(b64img_compressed)
    decompressed = pickle.loads(b64decoded) #zlib.decompress(b64decoded)
    #end = time.time_ns()
    #print(f'Start1: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')

    tracks = model_sample_model.track(
            decompressed,
            conf=0.6,
            persist=True,
            tracker="bytetrack.yaml",
            show=False,
            verbose=True,
        )
    end = time.time_ns()
    #print(f'Start2: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')

    tracksb64 = base64.b64encode(pickle.dumps(tracks[0].boxes))
    #tracksb64 = base64.b64encode(pickle.dumps({"aaa": 1}))
    #end = time.time_ns()
    #print(f'Start3: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')

    return tracksb64


#    b64decoded = base64.b64decode(b64img_compressed)
#    decompressed = b64decoded #zlib.decompress(b64decoded)
#    imgarr = np.frombuffer(decompressed, dtype=np.uint8).reshape(w, h, -1)
#    return imgarr.shape[2], np.mean(imgarr)
