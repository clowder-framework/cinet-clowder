FROM python:3.7

ARG VERSION="unknown"
ARG BUILDNUMBER="unknown"
ARG GITSHA1="unknown"

# environemnt variables
ENV VERSION=${VERSION} \
    BUILDNUMBER=${BUILDNUMBER} \
    GITSHA1=${GITSHA1} \
    STREAM=requests \
    RABBITMQ_QUEUE="ncsa.cinet.hydroshare"

WORKDIR /extractor
#COPY requirements.txt ./
#RUN pip install -r requirements.txt

RUN pip install hsclient

RUN mkdir /home/publisher

COPY hydroshare_publisher.py extractor_info.json ./
CMD python hydroshare_publisher.py

