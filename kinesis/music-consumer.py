import logging
import random
import mido
import json
import pygame

from kinesis.consumer import KinesisConsumer

from pygame.locals import *

from mido import Message

# from kinesis.state import DynamoDB

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(process)d %(name)s:%(lineno)d %(message)s')
logging.getLogger('botocore').level = logging.INFO
logging.getLogger('botocore.vendored.requests.packages.urllib3').level = logging.WARN

# buttons  
# 2 3 5
# 0 1 4


# notes = [80, 82, 84, 87, 89, 92, 94, 96, 98, 90]
notes = [80, 82, 89, 84, 87, 92, 94, 96, 98, 99]


# pygame.init()
port = mido.open_output() 

consumer = KinesisConsumer(stream_name='borgstrom-test')

for msg in consumer:

    print("msg:  ", format(msg))

    print("data: ", msg["Data"] )

    gh_event = json.loads(msg["Data"])

    print("gh_event: ", gh_event)
    

    if gh_event["type"] == JOYBUTTONDOWN:
        print("v")
        on = Message('note_on', note=notes[gh_event["button"]])
        port.send(on)

    elif gh_event["type"] == JOYBUTTONUP:
        print("^")
        off = Message('note_off', note=notes[gh_event["button"]])
        port.send(off)

    else:
        print("-")

