from flask import Flask, request, jsonify
from MLModel import process_image
from PIL import Image
import io
import os
import pathlib

app = Flask(__name__)


@app.route('/api/recieve_image', methods=["POST"])
def image_input():
    file = request.files.get('image', '')
    img = Image.open(file.stream)
    byteIO = io.BytesIO()
    img.save(byteIO, format='PNG')
    byteArr = byteIO.getvalue()

    return jsonify(
        {
            'msg': 'success',
            'result': process_image.predict_image(byteArr)
        })


@app.route('/api/submit_correction', methods=["POST"])
def submit_correction():
    file = request.files.get('image', '')
    file.save(os.path.join(pathlib.Path(__file__).parent.absolute(), file.filename))

    return jsonify({'msg':'success'})


@app.route('/')
def test():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
