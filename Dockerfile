FROM python:3.7

RUN mkdir /code
WORKDIR /code

COPY . /code/
RUN pip install pipenv 
RUN pipenv install --system --deploy

EXPOSE 5000
