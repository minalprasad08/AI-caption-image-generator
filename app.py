from flask import Flask, render_template, request
from model import generate_caption
import base64

app = Flask(__name__)

@app.template_filter('b64encode')
def b64encode_filter(data):
    return base64.b64encode(data).decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = ''
    image_data = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            image_bytes = file.read()
            caption = generate_caption(image_bytes)
            image_data = image_bytes

    return render_template('index.html', caption=caption, image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)
