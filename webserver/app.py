import time
import requests
from flask import Flask, send_file, request, render_template
from loguru import logger


app = Flask(__name__, static_url_path='')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def hello_world():
    data = request.data
    t = time.time()
    prediction = requests.get(f'http://localhost:8080/predict', data=data)
    total = time.time() - t
    logger.info(f'prediction took: {total}sec')
    return prediction.json()


if __name__ == '__main__':
    logger.info('starting MNIST web server...')
    app.run(host='0.0.0.0', port=8081)

