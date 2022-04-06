FROM python:3.9
WORKDIR /app/mail
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./mail .
EXPOSE 8002
CMD ["python3", "/app/mail/mail_server.py"]