#!/usr/bin/env python

import sys
import mido

from mido import Message

port = mido.open_output() 

def main(code):
    print("sysex ", code)
    sysex = Message('sysex', data=[code])
    port.send(sysex)

if __name__ == '__main__':
    code = sys.argv[1]
    main(int(code))

