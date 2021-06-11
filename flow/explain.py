#!/usr/bin/env python

import sys
import yaml

from mido import MidiFile

instrument_map = {}

def volume_sum(data):
    volume_sum = 0.0

    for instrument in data["instruments"]:
        volume = data["instruments"][instrument]["volume"] 
        volume_sum = volume_sum + volume

    return volume_sum  

def instruments(data):

    global instrument_map

    for instrument in data["instruments"]:
        program = data["instruments"][instrument]["program"]
        instrument_map.update({instrument : program})

def main(filename):

    with open(filename) as f:
        
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)

        instruments(data)
        print(instrument_map)

        print (volume_sum(data))   


if __name__ == '__main__':
    filename = sys.argv[1]  
    main(filename)  

    
