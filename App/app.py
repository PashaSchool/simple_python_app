from models.image import Image
from database.database import Database
from flask import Flask, render_template, request, send_file, make_response
import codecs


# from bson import Regex
from PIL import Image
# import io
# import cv2
# import numpy as np

# _______________________________________________
import tensorflow as tf
from datetime import datetime
import numpy as np
import os
import matplotlib.pyplot as plt

DIR = 'convolution/saved_model/'

import cv2
import io
# import PIL

# file_contents = tf.read_file('coala.jpg')
# image = tf.image.decode_jpeg(file_contents, channels=3)
# image = tf.image.resize_images(image,[ 32, 32])

# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     image_val = sess.run([image])
#     plt.figure(figsize=(16, 8))
#     print(image_val[0].shape)
#     plt.imshow(image_val[0].astype(np.uint8), interpolation='nearest')
#     plt.show()
#     plt.close() 

#######

# test_img = image_val[0]

# test_img = np.reshape(test_img, [1, 32, 32, 3]).astype(np.float32)
                    
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     tf.get_default_graph().as_graph_def()
    
#     saver = tf.train.import_meta_graph(os.path.join(DIR,'model-ckpt-4900.meta'))
#     saver.restore(sess, os.path.join(DIR,"model-ckpt-4900"))
#     print("restored")
    
#     x = tf.get_collection('training_data_input')[0]
#     y_true = tf.get_collection('training_data_outpuy')[0]
# #     accuracy = tf.get_collection('accuracy')[0]
#     y_predicted = tf.get_collection('prediction')[0]
#     keep_prob =  tf.get_collection('keep_prob')[0]
        
#     print("data is saved")

#     pred = sess.run(y_predicted, feed_dict={x: test_img , keep_prob: 1.0})
                                   
# print("testResult is — {}".format(pred))
# _______________________________________________

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
    img = Database.get_images()
    image = Database.FS.get(img[0]["fields"])

    base64_data = codecs.encode(image.read(), 'base64')
    image = base64_data.decode('utf-8')

    return index(images=image)
    

@app.route("/upload", methods=["POST"])
def upload_image():
    img_file = request.files['img']

    content_type = img_file.content_type
    filename = img_file.filename
    Database.save_to_mongo(img_file, content_type, filename)

    # file_contents = tf.image.decode_jpeg(img_file.read(), channels=3)
    # image = tf.image.decode_jpeg(img_file.read(), channels=3)
    # image = tf.image.resize_images(image,[ 32, 32])
    
    # with tf.Session() as sess:
    #     sess.run(tf.global_variables_initializer())
    #     tf.get_default_graph().as_graph_def()

    #     image_value = sess.run([image])
    #     reshaped_image = np.reshape(image_value[0], [1, 32, 32, 3]).astype(np.float32)

    #     saver = tf.train.import_meta_graph(os.path.join(DIR,'model-ckpt-4900.meta'))
    #     saver.restore(sess, os.path.join(DIR,"model-ckpt-4900"))
    #     print("restored")

    #     x = tf.get_collection('training_data_input')[0]
    #     y_true = tf.get_collection('training_data_outpuy')[0]
    #     y_predicted = tf.get_collection('prediction')[0]
    #     keep_prob =  tf.get_collection('keep_prob')[0]
    #     print("data is saved")

    #     pred = sess.run(y_predicted, feed_dict={x: reshaped_image , keep_prob: 1.0})
    #     print("THE PREDICTION IS LOOK LIKE THIS: {}".format(pred))


 
    # After I save the image ir byte coding
   ## img = Database.get_images()
   ## image = Database.FS.get(img[1]["fields"])
    # transform to array
   ## print("Image go to be transform")
   ## numpy_array_image = np.fromstring(image.read(), dtype=np.uint8) 
   ## cv2_image_decode = cv2.imdecode(numpy_array_image, cv2.IMREAD_COLOR) 
    ##print("Image transformet")
   ## print(cv2_image_decode.shape)

    return index(images=[])
    

if __name__ == '__main__':
    app.run(debug=True, port=5005)
