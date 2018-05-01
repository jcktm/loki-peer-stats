#!/bin/bash

for iter in $(seq 10)
do
  monero-v0.12.0.0/monerod --log-level 4 | grep last_seen | grep -v DEBUG | grep -v INFO > peers.txt &
  sleep 30
  pkill -9 monerod
  rm -rf ~/.bitmonero/

  python process.py < peers.txt
done
