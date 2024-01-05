FROM python:3.9-slim

# Install the latest version of Firefox
RUN apt-get update
RUN apt-get install -y xvfb
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y libcrypt1
RUN apt-get install -y firefox
RUN apt-get update                             \
  && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
  && rm -fr \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# Install the latest version of Geckodriver:
RUN BASE_URL=https://github.com/mozilla/geckodriver/releases/download \
  && VERSION=$(curl -sL \
    https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
    grep tag_name | cut -d '"' -f 4) \
  && curl -sL "$BASE_URL/$VERSION/geckodriver-$VERSION-linux64.tar.gz" | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl

# Install the requirements package and copy parser script
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY parser/ .
CMD ["python", "main.py"]
