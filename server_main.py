from flask import Flask, request, jsonify
from MLModel import process_image, label_func
from PIL import Image


app = Flask(__name__)

@app.route('/api/recieve_image', methods=["POST"])
def image_input():

    file = request.files.get('image', '')
    print(file)
    img = Image.open(file.stream)

    return jsonify(
        {
            'msg': 'success',
            'result': process_image.predict_image(img)
        })


@app.route('/')
def test():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
