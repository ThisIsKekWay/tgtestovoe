FROM python:3.9

WORKDIR .

COPY reqs.txt .

RUN pip install --upgrade pip

RUN pip install -r reqs.txt

COPY . .