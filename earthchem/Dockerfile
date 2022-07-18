FROM python:3.7

ARG VERSION="unknown"
ARG BUILDNUMBER="unknown"
ARG GITSHA1="unknown"

# environemnt variables
ENV VERSION=${VERSION} \
    BUILDNUMBER=${BUILDNUMBER} \
    GITSHA1=${GITSHA1} \
    STREAM=requests \
    RABBITMQ_QUEUE="ncsa.cinet.earthchem"

WORKDIR /extractor
#COPY requirements.txt ./
#RUN pip install -r requirements.txt

COPY pyclowder ./pyclowder
RUN pip install ./pyclowder && cd ..

RUN mkdir /home/publisher

COPY earthchem_publisher.py extractor_info.json ./
CMD python earthchem_publisher.py

