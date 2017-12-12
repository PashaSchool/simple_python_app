from models.image import Image
from database.database import Database
from flask import Flask, render_template, request, send_file, make_response


# from bson import Regex
from PIL import Image
import io
import cv2
import numpy as np

# from bitstring import BitArray

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

    image = Database.FS.get(img[1]["fields"])

    lst = Database.FS.get_version(img[1]["filename"])
    lst = lst.read()
    print(type(lst))
    import codecs
    base64_data = codecs.encode(lst, 'base64')
    image = base64_data.decode('utf-8')
    print(type(base64_data))
    return index(images=image)
    

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
