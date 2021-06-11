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


program_map = {}  # to be loafded from config

def load_config(filename="config.yaml"):
    global program_map

    with open(filename) as f:
        
        data = yaml.load(f, Loader=yaml.FullLoader)

        for track in data["tracks"]:
            program = data["tracks"][track]["instrument"]["program"]
            program_map.update({track : program})


def main(input, output="merged"):

    matcher = input + "/*.mid"

    collation = {}

    # collate mid files by track -----------------------

    for midi_filename in glob.glob(matcher):
        print("MIDI: ", midi_filename)
        matchObj = re.match(r'.*_(.*).mid', midi_filename)  # extract track name from filename

        if matchObj:
            track_name = matchObj.group(1)

            if track_name not in collation:
                print("- adding new track: ", track_name)
                collation[track_name] = MidiFile()

            new_midi_file = collation[track_name]

            # open midi file and append track to the track
            composed_midi_file = MidiFile(midi_filename)

            for i, track in enumerate(composed_midi_file.tracks):
                print("- ", track_name, " + ", track)
                new_midi_file.tracks.append(track)
        
    # now create midi tracks (by merging the parts) -------------------------

    for track, midi in collation.items():
        print(track)

        midi_file = MidiFile() 

        merged_track = merge_tracks(midi.tracks)
        merged_track.name = track

        # create new track and select program
        midi_program = program_map.get(track)

        midi_track = MidiTrack()

        midi_track.append(Message('program_change', program=midi_program, time=0)) # used for merged
        midi_track.extend(merged_track)

        midi_file.tracks.append(midi_track)
        midi_file.save(output + "/" + track + ".mid") # save the track midi


# MAIN -----------------------

if __name__ == '__main__':
    config  = sys.argv[1]
    input   = sys.argv[2]
    output  = sys.argv[3] 

    load_config(config)

    print("PROGRAM MAP: ", program_map)

    main(input, output)

