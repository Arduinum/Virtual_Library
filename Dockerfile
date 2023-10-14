FROM python:3.11.0

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./virtual_library ./
COPY requirements.txt ./virtual_library/requirements.txt
RUN pip3 install -r ./virtual_library/requirements.txt

COPY ./wait-for-postgres.sh .
RUN chmod +x ./wait-for-postgres.sh

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1