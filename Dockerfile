FROM python:3.9

ENV PYTHONUNBUFFERED 1

# Создание и переход в рабочую директорию
WORKDIR meganoapp/

COPY requirements.txt requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install Pillow

COPY diploma-frontend-0.6.tar.gz diploma-frontend-0.6.tar.gz

RUN pip install diploma-frontend-0.6.tar.gz

COPY meganoApp .





