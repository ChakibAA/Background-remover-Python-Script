from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
import requests

app = Flask(__name__)


@app.route('/remove_background', methods=['GET'])
def remove_background():
    try:
        image_url = request.args.get('image_url')

        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                img_bytes = response.content
                output_bytes = remove(img_bytes)
                return send_file(BytesIO(output_bytes), mimetype='image/png')
            else:
                return 'Image URL not accessible.', 400
        return 'Image URL not provided.', 400
    except Exception as e:
        return f"Error: {str(e)}", 500


@app.route('/', methods=['GET'])
def hello():
    return 'This is backgroud remover'


if __name__ == '__main__':
    app.run()
