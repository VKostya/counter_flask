FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install flask
RUN pip install psycopg2-binary
RUN pip install flask_sqlalchemy

COPY . /app

CMD ["python", "app.py"]