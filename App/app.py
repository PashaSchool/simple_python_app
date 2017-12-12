from models.image import Image
from database.database import Database
from flask import Flask, render_template, request, send_file, make_response


# from bson import Regex
from PIL import Image
import io
import cv2
import numpy as np

app = Flask(__name__)

@app.before_first_request 
def initiliae_database():
    Database.initialize()


@app.route("/")
def index(images=[]):
    return render_template("index.html", images=images)

@app.route('/get_all_images')
def get_image():
    # images = Image.get_images()

    img = Database.get_images()
    # print(type(img))
    # print(img[0]["filename"])

    image = Database.FS.get(img[0]["fields"])
    # print(image.read())
    # image = image.read()
    lst = Database.FS.get_version(img[0]["filename"])


    # print(lst)
    # img = io.BytesIO(lst)
    # print(str(lst))
    # print(img.read())
    # nparray = np.fromstring(lst.read(), np.uint8)
    # img_np = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    # image = cv2.imshow('yyy', img_np)
    # print(type(image))
    ## pas img 
    # image.show()

    # if len(images) > 0:
    #     return index(images)
    # print("The image is {}".format(image))
    # print(img_np.shape)

    return index(images=lst.read())
    

@app.route("/upload", methods=["POST"])
def upload_image():
    img_file = request.files['img']
    content_type = img_file.content_type
    filename = img_file.filename
    print(img_file)

    Database.save_to_mongo(img_file, content_type, filename)

    return index(images=[])
    

if __name__ == '__main__':
    app.run(debug=True, port=5005)
