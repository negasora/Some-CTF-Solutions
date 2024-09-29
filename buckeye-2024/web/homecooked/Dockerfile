FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get install -y \
    autoconf \
    bison \
    flex \
    gcc \
    g++ \
    git \
    libprotobuf-dev \
    libnl-route-3-dev \
    libtool \
    make \
    pkg-config \
    protobuf-compiler \
    uidmap \
    && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/google/nsjail && \
    cd nsjail && \
    make -j8 && \
    mv nsjail /bin && \
    cd / && \
    rm -rf nsjail

FROM python:3.12-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive
COPY --from=0 /usr/bin/nsjail /usr/bin/

RUN useradd -m ctf && \
mkdir /chroot/ && \
chown root:ctf /chroot && \
chmod 770 /chroot

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY homecooked ./homecooked
COPY static ./static
COPY templates/ ./templates
COPY main.py chef.py jail.cfg ./
COPY flag.txt /flag.txt
COPY start_server.sh ./
RUN cp /bin/sh /bin/sh-orig
RUN chown -R root:ctf . && \
    chmod 440 /flag.txt
RUN chmod +x start_server.sh


EXPOSE 8000
ENTRYPOINT ["/app/start_server.sh"]

