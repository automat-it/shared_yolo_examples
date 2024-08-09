import grpc

# import the generated classes
import yolo_pb2
import yolo_pb2_grpc

# data encoding

import numpy as np 
import base64
import zlib
import time
import cv2
import pickle
#import cPickle as pickle


# open a gRPC channel
channel = grpc.insecure_channel('127.0.0.1:8001')

# create a stub (client)
stub = yolo_pb2_grpc.ImageProcedureStub(channel)

# encoding image/numpy array

#for _ in range(1000):
image = cv2.imread("test_image.jpg")
image = cv2.resize(image, (480, 480))
# compress
#data = zlib.compress(frame)
for i in range(1, 5):
    print(f'RUN {i} -----------------------------------------')
    start = time.time_ns()
    data = base64.b64encode(pickle.dumps(image))
    # create a valid request message
    #end = time.time_ns()
    #print(f'Start: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')
    #start = time.time_ns()

    image_req = yolo_pb2.B64Image(b64image = data, width = 416, height = 416)
    # make the call
    response = stub.ImageMeanWH(image_req)
    #end = time.time_ns()
    #print(f'Start: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')

    b64decoded = base64.b64decode(response.b64response)
    res = pickle.loads(b64decoded) 

    end = time.time_ns()
    print(f'Start: {start}, End: {end}, Exec time:{(end-start)/1000000} ms')
    #print(decompressed)
    boxes = res.xyxy.cpu()
    clss = res.cls.cpu().tolist()
    track_ids = res.id.int().cpu().tolist()
    for box, track_id, cls in zip(boxes, track_ids, clss):
        print(f'Track: {track_id}, Class:{cls}, Box:{box}')

