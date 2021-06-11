#!/usr/bin/env sh

CONFIG=$1
echo "MASTERING: $CONFIG"

sox output/mix/mix.wav \
    output/master/master.wav \
    compand 0.3,1 6:-70,-60,-20 -5 -90 0.2

    # contrast 10