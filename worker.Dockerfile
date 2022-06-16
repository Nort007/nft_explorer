FROM python:3.10.4-buster

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER_=workerr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/home/${USER_}/src/app"
RUN apt-get update && apt-get upgrade -y
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

RUN pip3 install --user --upgrade pip
RUN pip3 install --user celery redis aiohttp aiodns python-dotenv

COPY --chown=${USER_}:${USER_} start_worker.sh .
COPY --chown=${USER_}:${USER_} api/ api/
COPY --chown=${USER_}:${USER_} core/ core/
COPY --chown=${USER_}:${USER_} db/ db/
COPY --chown=${USER_}:${USER_} .env .env
#RUN chmod +x start_worker.sh
