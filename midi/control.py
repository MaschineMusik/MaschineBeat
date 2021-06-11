#!/usr/bin/env python

import sys
import mido

from mido import Message

port = mido.open_output() 


# note on  = 0-9
# start = 10-15-240
# stop = 2-11-176
# reset = 15-15-240

def main(value):
    print("control ", value)
    control = Message('control_change', control=value)
    port.send(control)

if __name__ == '__main__':
    value = sys.argv[1]
    main(int(value))


