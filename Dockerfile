### test commit
FROM python:3.8
RUN pip3 install pika flask
COPY simple_server.py .
CMD ["python","simple_server.py"]
