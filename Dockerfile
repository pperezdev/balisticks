FROM python:3.8

WORKDIR /tmp

COPY . /tmp

ARG env_flask_variable_web=webapp/app 
ARG env_flask_variable_api=webapi/app 

ENV FLASK_WEBAPI=$env_flask_variable_web 
ENV FLASK_WEBAPP=$env_flask_variable_api 

RUN pip install -r requirements.txt
