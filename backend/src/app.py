from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS
import os
import ellipticCurve as ec
import imgToDat



app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/imageUpload', methods=['POST'])
def imageUpload():
    if 'image' not in request.files:
        return 'No image file uploaded', 400

    image = request.files['image']
    if image.filename == '':
        return 'No selected image file', 400

    # Create the "img" folder if it doesn't exist
    if not os.path.exists('./img'):
        os.makedirs('./img')

    # Save the image to the "img" folder
    image.save(os.path.join('./img', image.filename))
    path = os.path.join('./img', image.filename)

    return path

@app.route('/encDecImage', methods=['POST'])
def encryptImage():
    path = imageUpload()
    enc = ec.encrypt_to_disk(path)
    decryptImage(enc)
    encrypted_path = "static/encrypted_image.png"
    return send_file(encrypted_path, mimetype='image/png', as_attachment=True)


def decryptImage(enc):
    de = ec.decrypt_to_pic(enc)
    imgToDat.restoreImg(de, "static/decrypted_image.png")