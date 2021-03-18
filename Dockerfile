FROM python:3.8-slim-buster

RUN pip3 install pandas colorama

COPY . .

CMD ["python3", "main.py"]