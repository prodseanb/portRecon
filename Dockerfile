FROM python:3.9.5

ADD run.py .

ADD banner.py .

ENTRYPOINT ["python3", "./run.py"]