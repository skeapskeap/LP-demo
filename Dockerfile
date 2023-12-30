FROM python:3.11.7-slim

WORKDIR /app/

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY flask_app.py /app/

CMD flask --app flask_app run --host 0.0.0.0
