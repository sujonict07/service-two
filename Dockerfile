FROM python:3.6

# root directory for our project in the container

RUN mkdir /service-one

# working directory
WORKDIR /service-one

# copy requirements.txt file
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

# copy the current directory contents into the container
ADD micro_service_two /service-one/
