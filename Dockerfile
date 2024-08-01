FROM nvidia/cuda:12.5.1-runtime-ubuntu24.04

RUN apt update && \
    apt install -y python3 pip ffmpeg libsm6 libxext6 #.htop libgl1-mesa-glx libglib2.0-0

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt --break-system-packages
WORKDIR /app
COPY . /app
