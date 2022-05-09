FROM python:3.8.12-slim-buster
WORKDIR /app
COPY . .
COPY ./pip.conf /pip.conf
ENV PIP_CONFIG_FILE /pip.conf
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

CMD ["python3", "live_mnist.py"]