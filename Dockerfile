FROM python:3.10.8

RUN pip install FLask

WORKDIR /lab3

COPY /lab3 .

EXPOSE 5001

CMD ["python", "api.py"]