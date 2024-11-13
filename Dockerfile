FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

COPY . /app

CMD ["python", "app.py"]