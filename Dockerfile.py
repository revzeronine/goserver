FROM debian:stable-slim

RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip

COPY main.py main.py
COPY books/ books/

CMD ["python3", "main.py"]