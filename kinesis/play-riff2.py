import logging
import os
import json
import subprocess

import pygame

from pygame.locals import *


from kinesis.consumer import KinesisConsumer


dir = "/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/"

chords = ['/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-A.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-B.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-C.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-D.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-E Hi.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-E Lo.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-F.wav',
         '/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/HMRhyCPwrchord-G.wav',
         ]


# from kinesis.state import DynamoDB

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(process)d %(name)s:%(lineno)d %(message)s')
logging.getLogger('botocore').level = logging.INFO
logging.getLogger('botocore.vendored.requests.packages.urllib3').level = logging.WARN



consumer = KinesisConsumer(stream_name='borgstrom-test')

for msg in consumer:

    print("msg:  ", format(msg))

    print("data: ", msg["Data"] )

    gh_event = json.loads(msg["Data"])

    print("button: ", gh_event["button"] )
    

    if gh_event["type"] == JOYBUTTONDOWN:
        sound = chords[gh_event["button"]]
        command = 'aplay ' + '"' + sound + '"'
        print(command)
        subprocess.Popen(["aplay", sound])
