# DL_Project
## Goal
- The project is based on the virtual try-on project(https://github.com/jiayunz/Virtual-Try-On). The goal is to understand and present a pipeline that can help virtually try on clothes by uploading a picture.
- The pipeline is wrapped with a flask/angular based application
## Links
- The Project presentations, videos and notebooks that explain the different models are all present in the Google Drive below. 
      https://drive.google.com/drive/folders/1LkAeDhEOaWGS9ZRdYRgE4xhKthTUbWJa?usp=sharing
## Installation Instructions
- Download and Install OpenPose in the OpenPose Directory. The installation instructions and files are available in the below location. Please ensure that BUILD_PYTHON is enabled.
- Add the models in the cp_vton/checkpoints and LIP_JPPNet/checkpoint from the below location:
      https://drive.google.com/drive/folders/1tbfB9xl2veejq_m9lcSNnRXTYp11lENn?usp=sharing
- Ensure that all the paths are corrected to wherever you are downloading the code to in the following files (try_on.py, cp_vton/test.py, LIP_JPPNet/evaluate_parsing_JPPNet.py)
- The required libraires are : Python-3.6.5, Tensorflow-1.13.1, pytorch-1.3.0, torchvision-0.2.1, Flask and Angular
- Angular, Node and NPM can be installed using the instructions here (https://nodejs.org/en/download/)
- Download and Install Matlab, Use the Matlab library browser to install Matlab Image Processing Library.
## Running Instructions
- Open the command line to the api directory and run the following commands
- SET FLASK_APP = com.datacorps.rest.app
  flask run
- Open the command line to the frontend directory and run the following command
  ng serve
- This will open the frontend application in localhost:4200/
## VTON Code Repo With Modification
https://github.com/YuxingW/cp-vton.git
## References
Cp-Vton in github: https://github.com/sergeywong/cp-vton <br />
Vton paper in arxiv:https://arxiv.org/pdf/1807.07688.pdf
