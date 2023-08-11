FROM joyzoursky/python-chromedriver:3.9

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY parser/ .

CMD ["python", "main.py"]
