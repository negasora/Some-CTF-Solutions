# echo 'hxp{FLAG}' > flag && docker build -t compilerbot . && docker run --cap-add=SYS_ADMIN --security-opt apparmor=unconfined -ti -p 8011:1024 compilerbot

FROM debian:buster

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        llvm clang python3

RUN useradd --create-home --shell /bin/bash ctf
WORKDIR /home/ctf
COPY service.py flag /home/ctf/
COPY ynetd /sbin/

RUN chmod 555 /home/ctf && \
    chown -R root:root /home/ctf && \
    chmod -R 000 /home/ctf/* && \
    chmod 500 /sbin/ynetd && \
    chmod 444 /home/ctf/flag && \
    chmod 005 /home/ctf/service.py

# check whitelist of writable files/folders
USER ctf
RUN (find --version && id --version && sed --version && grep --version) > /dev/null
RUN ! find / -writable -or -user $(id -un) -or -group $(id -Gn|sed -e 's/ / -or -group /g') 2> /dev/null | grep -Ev -m 1 '^(/dev/|/run/|/proc/|/sys/|/tmp|/var/tmp|/var/lock)'
USER root

EXPOSE 1024
CMD ynetd -lm 134217728 -lt 1 -sh n /home/ctf/service.py
