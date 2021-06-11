#!/usr/bin/env python
"""
Merge a folder of midi files in to a single midi file
"""
import sys
import time
import re
import yaml

import mido

import glob

from mido import MidiFile, MidiTrack, Message, merge_tracks


instrument_map = {}  # to be loafded from config

def load_config(filename="config.yaml"):
    global instrument_map

    with open(filename) as f:
        
        data = yaml.load(f, Loader=yaml.FullLoader)

        for instrument in data["instruments"]:
            program = data["instruments"][instrument]["program"]
            instrument_map.update({instrument : program})


def main(input, output="merged"):

    matcher = input + "/*.mid"

    collation = {}

    # collate mid files by instrument -----------------------

    for midi_filename in glob.glob(matcher):
        matchObj = re.match(r'.*_(.*).mid', midi_filename)  # extract instrument name from filename

        if matchObj:
            instrument = matchObj.group(1)

            if instrument not in collation:
                collation[instrument] = MidiFile()

            instrument_midi = collation[instrument]

            # open midi file and append track to the instrument
            midi_file = MidiFile(midi_filename)

            for i, track in enumerate(midi_file.tracks):
                instrument_midi.tracks.append(track)

    # now create instrument tracks (by merging the parts) -------------------------

    for instrument, midi in collation.items():
        print(instrument)

        instrument_midi = MidiFile() 

        merged_track = merge_tracks(midi.tracks)
        merged_track.name = instrument

        # create new track and select instrument
        midi_instrument = instrument_map.get(instrument)

        instrument_track = MidiTrack()

        instrument_track.append(Message('program_change', program=midi_instrument, time=0)) # used for merged
        instrument_track.extend(merged_track)

        instrument_midi.tracks.append(instrument_track)
        instrument_midi.save(output + "/" + instrument + ".mid") # save the instrument midi


    # now create a new midi file with merged tracks (and selected instruments)

    compilation = MidiFile() 

    for instrument, midi in collation.items():

        merged_track = merge_tracks(midi.tracks)
        merged_track.name = instrument

        # create new track and select instrument
        instrument_track = MidiTrack()
        midi_instrument = instrument_map.get(instrument)
        instrument_track.append(Message('program_change', program=midi_instrument, time=0)) # used for merged

        compilation.tracks.append(instrument_track)

    compilation.save(output + "/../merged/merged.mid")  # save the composition midi


# MAIN -----------------------

if __name__ == '__main__':
    input   = sys.argv[1]
    output  = sys.argv[2] 

    load_config("config.yaml")
    main(input, output)

