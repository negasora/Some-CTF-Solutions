FROM node:22 AS chroot
WORKDIR /src

COPY *.json ./
RUN npm install

RUN mkdir /opt/bad-todo

COPY *.js ./
COPY .env ./
COPY views ./views
COPY entry.sh /home/user/entry.sh


CMD /home/user/entry.sh
