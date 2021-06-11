#!/usr/bin/env bash

CONFIG=$1

echo "RECORDING: $CONFIG"

for midi in output/arrange/*.mid
do
    input=$(basename $midi)
    track=${input/.mid/}

    instrument=$(shyaml get-value tracks.$track.instrument < $CONFIG)
    soundfont=$(shyaml get-value tracks.$track.instrument.soundfont.file < $CONFIG)

    echo - TRACK: $track = INST $instrument

    fluidsynth -i \
        -F output/record/$track.wav \
        -g 0.5 \
        sounds/$soundfont \
        $midi
done

