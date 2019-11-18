from python:3.7.4

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

# COPY ./app.py ./app.py
# COPY ./client/ ./client/

ENTRYPOINT ["python", "app.py"]

