import grpc
from concurrent import futures
import time

import yolo

# import the generated classes
import yolo_pb2
import yolo_pb2_grpc


# based on .proto service
class ImageProcedureServicer(yolo_pb2_grpc.ImageProcedureServicer):

    def ImageMeanWH(self, request, context):
        response = yolo_pb2.Prediction()
        response.b64response  = yolo.predict(request.b64image, request.width, request.height)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=12))


# add the defined class to the server
yolo_pb2_grpc.add_ImageProcedureServicer_to_server(
        ImageProcedureServicer(), server)

# listen on port 5005
print('Starting server. Listening on port 8001.')
server.add_insecure_port('[::]:8001')
server.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    server.stop(0)
