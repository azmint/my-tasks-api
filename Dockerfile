FROM python:3.8-slim

RUN apt-get update
RUN apt-get -y install locales vim less curl && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./src /opt
COPY ./Pipfile.lock /opt/Pipfile.lock

WORKDIR opt
RUN pipenv sync --system

CMD ["gunicorn", "boot:app", "-b", "0.0.0.0:8080"]
EXPOSE 8080