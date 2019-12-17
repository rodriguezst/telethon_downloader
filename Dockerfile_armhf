FROM balenalib/armv7hf-ubuntu:bionic
MAINTAINER rodriguezst <github.com/rodriguezst>

RUN [ "cross-build-start" ]

COPY tg_downloader.py /app/tg_downloader.py

RUN apt-get update && apt-get install -y --no-install-recommends \
                                python3 \
                                python3-dev \
                                libffi-dev \
                                python3-pip \
                                python3-setuptools \
                                python3-wheel \
                                build-essential \
                && rm -rf /var/lib/apt/lists/* \
                && pip3 install cryptg \
                && pip3 install telethon[cryptg] \
                && apt-get remove --purge -y build-essential \
                                python3-dev \
                                libffi-dev \
                && apt autoremove -y \
                && rm -rf /var/lib/apt/lists/* \
                && chmod +x /app/tg_downloader.py \
                && chown 1000:1000 /app/tg_downloader.py

RUN [ "cross-build-end" ]

USER 1000:1000
WORKDIR /app
ENTRYPOINT ["/app/tg_downloader.py"]
