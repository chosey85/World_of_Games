FROM python:3.8-alpine

WORKDIR /app

COPY Utils.py .
COPY scores.txt .
COPY MainScores.py .

RUN pip install flask

CMD ["python", "MainScores.py"]