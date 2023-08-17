FROM joyzoursky/python-chromedriver:latest

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY parser/ .

CMD ["python", "main.py"]
