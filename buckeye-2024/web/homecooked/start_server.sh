#!/bin/bash

mkdir -p /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
chown ctf /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
cp sh /bin/sh

exec uvicorn main:app --host 0.0.0.0

