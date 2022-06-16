FROM python:3.10.4-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/home/nftuser/src/app"
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN apt-get update && apt-get upgrade -y
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
COPY --chown=nftuser:nftuser start_worker.sh .
COPY --chown=nftuser:nftuser api/ api/
COPY --chown=nftuser:nftuser core/ core/
COPY --chown=nftuser:nftuser db/ db/
COPY --chown=nftuser:nftuser .env .env
RUN chmod +x start_worker.sh