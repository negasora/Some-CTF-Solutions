#!/bin/bash

pipenv run git-dumper https://gitgoo.challs.pwnoh.io/ out/

pushd out || exit

git checkout 872e509
cat flag.txt

popd || exit
