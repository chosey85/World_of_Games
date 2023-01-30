FROM python:alpine

RUN mkdir -p etc
ADD etc/utils.py etc/utils.py
ADD scores.txt .
ADD MainScores.py .

CMD ["python3", "./MainScores.py"]