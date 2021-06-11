#!/usr/bin/env python

import sys
import mido

from mido import Message

port = mido.open_output() 

def main(note):
    print("NOTE ", note)
    on = Message('note_on', note=note)
    port.send(on)

if __name__ == '__main__':
    note = sys.argv[1]
    main(int(note))

