FROM python:3.9-slim

# Install Firefox browser and GeckoWebDriver
RUN apt-get update
RUN apt-get install -y xvfb
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y libcrypt1
RUN apt-get install -y firefox
RUN apt-get update                             \
 && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl

# Install the requirements package and copy parser script
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY parser/ .
CMD ["python", "main.py"]
