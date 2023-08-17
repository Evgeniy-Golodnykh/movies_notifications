FROM python:3.9-slim

RUN apt-get update -y
# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get install -y gnupg wget curl unzip --no-install-recommends
# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable
# Find Chromedriver Version
ENV CHROME_VERSION $(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*")
ENV DRIVER_VERSION $(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
# Download and install Chromedriver
RUN wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip /chromedriver/chromedriver* -d /chromedriver
# Set display port as an environment variable
ENV DISPLAY=:99

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY parser/ .

CMD ["python", "main.py"]
