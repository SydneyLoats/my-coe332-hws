FROM centos:7.9.2009

RUN yum update -y
RUN yum install -y python3

RUN pip3 install names==0.3.0
RUN pip3 install --user redis
RUN pip3 install --Flask==2.0.3

RUN mkdir /app
WORKDIR /app
COPY ML_Data_Sample.json /app
COPY app.py /app
COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
