FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY calculator.py /app/calculator.py
COPY caltest.py /app/caltest.py

CMD ["python3",  "calculator.py"]
