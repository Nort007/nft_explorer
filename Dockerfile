FROM python:3.10.4-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/home/nftuser/src/app"
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y nano xvfb chromium-driver htop


RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*


#Create user
RUN groupadd -g ${GROUP_ID} nftuser &&\
    useradd -l -u ${USER_ID}  -g nftuser nftuser &&\
    install -d -m 0755 -o nftuser -g nftuser /home/nftuser &&\
    chown --changes --silent --no-dereference --recursive \
    --from=33:33 ${USER_ID}:${GROUP_ID} \
    /home/nftuser

WORKDIR /home/nftuser

RUN mkdir -p src/app
RUN chown -R nftuser:nftuser .

USER nftuser

WORKDIR src/app

COPY --chown=nftuser:nftuser ./requirements.txt .

RUN pip3 install --user --upgrade pip

RUN pip3 install --user -r requirements.txt

ENV PATH="${HOME}/.local/bin:${PATH}"

# Копировать код
COPY --chown=nftuser:nftuser bot_v01/ bot_v01/
COPY --chown=nftuser:nftuser db/ db/
COPY --chown=nftuser:nftuser delivery_club/ delivery_club/
COPY --chown=nftuser:nftuser docs/ docs/
COPY --chown=nftuser:nftuser gem/ gem/
COPY --chown=nftuser:nftuser opensea/ opensea/
COPY --chown=nftuser:nftuser .env .env