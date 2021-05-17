from flask import Flask
import io
import os
from base64 import b64encode,b64decode
from flask import jsonify,request,make_response
from flask_cors import CORS, cross_origin
from subprocess import call
import sys
import h5py

sys.path.insert(0, "D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/")
from try_on import *

from PIL import Image
# from flask import jsonify
app = Flask(__name__)

CORS(app, resources=r'/api/*')
OPEN_POSE = "D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/OpenPose/build/x64/Release/OpenPoseDemo.exe"
OPEN_POSE_DIR = "D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/OpenPose/"
UPLOAD_FOLDER = 'D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/data/raw_data/image'
SOURCE_FOLDER = 'D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/data/raw_data/'
TARGET_FOLDER = 'D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/data/test/'
JSON_DIR = "D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/data/raw_data/pose"
RESULT_DIR = "D:/Learning/Fall2020/Spring2021/DeepLearning/Project/DLCode/Virtual-Try-On-master/result/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='JPEG')# convert the PIL image to byte array
    img_data = byte_arr.getvalue()
    img_data = b64encode(img_data)
    if not isinstance(img_data, str):
        # Python 3, decode from bytes to string
        img_data = img_data.decode()
    img_data = "data:image/jpg;base64,"+img_data
    return img_data


@app.route("/api/get_images")
def get_cloth_images():
    # server side code
    path = os.getcwd() + "/assets/images"
    image_data = []
    for filename in os.listdir(path):
        if filename.find("thumbnail") != -1:
            image_data.append({"img": filename.replace(".thumbnail",""), "url": get_response_image(path+"/"+filename)})
    response = {'Status': 'Success',  'ImageBytes': image_data}
    return jsonify(response)


@app.route("/api/post_user_image", methods=['GET', 'POST'])
def get_tryon_image():
    if request.method == 'POST':
        if os.path.isfile(UPLOAD_FOLDER + '/model_to_dress.jpg'):
            os.remove(UPLOAD_FOLDER + '/model_to_dress.jpg')
        if os.path.isfile(JSON_DIR+ '/model_to_dress_keypoints.json'):
            os.remove(JSON_DIR + '/model_to_dress_keypoints.json')
        data = request.get_json()["fileSource"].replace("data:image/jpeg;base64,","")
        image_data = bytes(data, encoding="ascii")
        im = Image.open(io.BytesIO(b64decode(data)))
        im.save(os.path.join(app.config['UPLOAD_FOLDER'], "model_to_dress.jpg"))
        params = " --image_dir "+ UPLOAD_FOLDER + " --model_pose COCO - -write_json " +JSON_DIR
        status = call(OPEN_POSE+" "+params, cwd=OPEN_POSE_DIR)
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}

    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}



@app.route("/api/get_clothing", methods=['GET', 'POST'])
def get_clothing():

    if request.method == 'POST':
        image_name = request.get_json()["imageName"]
        run_model(source_root_dir=SOURCE_FOLDER, target_root_dir=TARGET_FOLDER, imname='model_to_dress.jpg',cname=image_name)
        # server side code
        path = RESULT_DIR+"model_to_dress.jpg"
        response = {'Status': 'Success', 'ImageBytes': {"img": "result", "url": get_response_image(path)}}
        return jsonify(response)
