FROM python:3.9
WORKDIR /app/myapp
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./myapp .
EXPOSE 8001
CMD ["python3", "/app/myapp/server.py"]