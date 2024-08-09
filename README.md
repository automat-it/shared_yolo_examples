THIS CODE PROVIDED AS AN EXAMPLE AND SHOULD NOT BE USED FOR PRODUCTION SYSTEMS

The repo contains all necesarry files to build docker image and run it on standalone GPU instance or on Kubernetes.

Prerequriment:
1. Install docker
2. Install Nvidia GPU driver:
https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html
3. Install Nvidia container toolkit:
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html



Build docker image
1. Run command:
docker build . -t yolo-gpu-test
2. Optionally push the image to the ECR to test the model on Kubernetes cluster.


How to run tests on GPU instance?

1. Execute the folloiwng command once to run the test application on local GPU instance or multiple times to simulate multiple copies of the application:
docker run --gpus all yolo-gpu-test -- python3 client_local.py

2. To check GPU utilization execute the command:
docker run --gpus all yolo-gpu-test -- nvidia-smi



How to run tests on Kubernetes?


1. update the folloiwng part of the yolo-test-deployment.yaml:
      - command:
        - python3
        - "client_local.py"
        - "<sleep time>"
        image: <ECR repo with the the image>

Where <sleep time> - timeout between model_sample_model.track executions. Assuming of video flow is 24 frames per second the timeout chould be 1/24 = 0.04
	<ECR repo with the the image> - ECR repo name and tag of the docker image.

2. Apply the deployment on Kubernetes cluster:
kubectl apply -f yolo-test-deployment.yaml

3. To change amount of model pods update 'replicas' value and apply the deployment file again.

4. To delete deployment execute:
kubectl delete -f yolo-test-deployment.yaml


5. Performance results:
GPU utilization:
- Find one of the deployemnt pod by command:

- Execute nvidia-smi command on the pod:
kubectl exec -it <POD_NAME> -- nvidia-smi

Data processing speed:
- Find one of the deployemnt pod by command:

- Get logs of the pod by command:
kubectl logs <POD_NAME>


Troubleshuting:
The most command problem is that docker run or pod does not have access to GPU in this case "WARNING: The NVIDIA Driver was not detected.  GPU functionality will not be available." warning messages appers and client_local.py exits with error.

==========
== CUDA ==
==========

CUDA Version 12.5.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

WARNING: The NVIDIA Driver was not detected.  GPU functionality will not be available.
   Use the NVIDIA Container Toolkit to start this container with GPU support; see
   https://docs.nvidia.com/datacenter/cloud-native/ .


In this case for Docker execution need to check that Nvidia driver is installed and the docker executed with --gpus all option.
For Kubernetes need to check on which node a pod are running and has correct XXXXX variable that should be:



