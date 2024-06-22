FROM python:3.8
WORKDIR /iris-demo
COPY . /iris-demo
RUN pip3 install -r requirements.txt
EXPOSE 8000
LABEL authors="Artem Polozov"
ENTRYPOINT ["./docker-entrypoint.sh"]
