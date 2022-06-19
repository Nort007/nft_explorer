FROM python:3.10.4-buster

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER_=nftuser
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/home/${USER_}/src/app"

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
RUN groupadd -g ${GROUP_ID} ${USER_} &&\
    useradd -l -u ${USER_ID}  -g ${USER_} ${USER_} &&\
    install -d -m 0755 -o ${USER_} -g ${USER_} /home/${USER_} &&\
    chown --changes --silent --no-dereference --recursive \
    --from=33:33 ${USER_ID}:${GROUP_ID} \
    /home/${USER_}

WORKDIR /home/${USER_}

RUN mkdir -p src/app
RUN chown -R ${USER_}:${USER_} .

USER ${USER_}

WORKDIR src/app

COPY --chown=${USER_}:${USER_} ./requirements.txt .

RUN pip3 install --user --upgrade pip

RUN pip3 install --default-timeout=300 --user -r requirements.txt

ENV PATH="${HOME}/.local/bin:${PATH}"

# Копировать код
COPY --chown=${USER_}:${USER_} bot_v01/ bot_v01/
COPY --chown=${USER_}:${USER_} db/ db/
COPY --chown=${USER_}:${USER_} delivery_club/ delivery_club/
COPY --chown=${USER_}:${USER_} gem/ gem/
COPY --chown=${USER_}:${USER_} opensea/ opensea/
COPY --chown=${USER_}:${USER_} selenium_tools/ selenium_tools/
COPY --chown=${USER_}:${USER_} .env.example .env.example