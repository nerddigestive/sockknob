FROM ubuntu:16.04

MAINTAINER Ed Hill "edhill@nerddigestive.com"

EXPOSE 5000/tcp

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]
