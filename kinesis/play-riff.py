import logging
import random
import mido
import json
import pygame

from kinesis.consumer import KinesisConsumer

from pygame.locals import *

from mido import Message

#coding=utf-8  

import pyaudio  
import wave  

#define stream chunk   
chunk = 1024  

dir = "/home/jan/media/musicradar-heavy-metal-samples/Guitar C/Power chords C/"

notes = ['HMRhyCPwrchord-A.wav',
         'HMRhyCPwrchord-B.wav',
         'HMRhyCPwrchord-C.wav',
         'HMRhyCPwrchord-D.wav',
         'HMRhyCPwrchord-E Hi.wav',
         'HMRhyCPwrchord-E Lo.wav',
         'HMRhyCPwrchord-F.wav',
         'HMRhyCPwrchord-G.wav',
         ]

# from kinesis.state import DynamoDB

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(process)d %(name)s:%(lineno)d %(message)s')
logging.getLogger('botocore').level = logging.INFO
logging.getLogger('botocore.vendored.requests.packages.urllib3').level = logging.WARN



consumer = KinesisConsumer(stream_name='borgstrom-test')

for msg in consumer:

    print("msg:  ", format(msg))

    print("data: ", msg["Data"] )

    gh_event = json.loads(msg["Data"])

    print("gh_event: ", gh_event)
    

    if gh_event["type"] == JOYBUTTONDOWN:
        print("v")
        note = notes[gh_event["button"] - 1]

        #open a wav format music  
        f = wave.open(dir + note,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

#close PyAudio  
p.terminate()  
