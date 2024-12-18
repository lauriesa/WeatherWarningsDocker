FROM python:3.8

WORKDIR /warnings-api

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python",   "./src/app.py"]