FROM python:3.9
WORKDIR /app/database
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./database .
EXPOSE 8002
CMD ["python3", "/app/database/db_server.py"]