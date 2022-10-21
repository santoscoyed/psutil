FROM python:3.10

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN pip install psutil

COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "./health_monitor.py"]
