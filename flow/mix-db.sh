#!/usr/bin/env bash

CONFIG=$1
echo "MIXING: $CONFIG"

sox_cmd="sox -m "



# add up total volume -----------

total_volume=0

for wav in output/record/*.wav
do
    input=$(basename $wav)
    track=${input/.wav/}

    volume=$(shyaml get-value tracks.$track.volume < $CONFIG)

    total_volume=$(($total_volume + volume))
done


echo "TOTAL VOLUME: $total_volume"

volume_normaliser="0.8"

# make the master
# normalise volumes to add up to 0.8

for wav in output/record/*.wav
do
    input=$(basename $wav)
    track=${input/.wav/}

    volume=$(shyaml get-value tracks.$track.volume < $CONFIG)

    normalised_volume=$(dc <<< "3 k $volume $total_volume / $volume_normaliser * p ")

    echo "- $track @ $volume => $normalised_volume"

    sox_cmd="$sox_cmd -v $normalised_volume $wav"
done

sox_cmd="$sox_cmd output/mix/mix.wav gain -b -n"

echo  $sox_cmd

($sox_cmd)