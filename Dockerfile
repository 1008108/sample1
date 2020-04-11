FROM python:2.7

ADD mac_request.py /

RUN pip install requests

ENTRYPOINT ["python", "mac_request.py"]

