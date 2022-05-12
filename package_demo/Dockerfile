FROM python:3.8.12-slim-buster
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN py get-pip.py
RUN pip install twine
RUN  pip install wheel

CMD ["python3", "ascii.py"]