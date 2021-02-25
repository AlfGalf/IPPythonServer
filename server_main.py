from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/recieve_image', methods=["POST"])
def image_input():

    files = request.files.to_dict(flat=False)
    print(files)
    for i, file in enumerate(files):
        print(file)
        files[file][0].save(f'image-{i}.jpg')

    return jsonify(
        {
            'msg': 'success',
            'result': 'a'
        })

@app.route('/')
def test():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
