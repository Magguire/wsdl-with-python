FROM python:3.10-slim

MAINTAINER "elizabeth.kihungi@abcthebank.com"

ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /project/

COPY requirements.txt .

RUN pip3 install --upgrade pip

#RUN pip install djangorestframework
#RUN pip install wheel
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

ARG ENV=dev

CMD ["python3","main.py"]