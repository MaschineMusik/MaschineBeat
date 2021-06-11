from __future__ import print_function

import sys
import time
import random
import mido
import logging
import pygame
import json

from mido import Message
from pygame.locals import *


from kinesis.producer import KinesisProducer

logging.basicConfig(level=logging.DEBUG, format='%(created)f %(levelname)s %(process)d %(name)s:%(lineno)d %(message)s')
logging.getLogger('botocore').level = logging.INFO
logging.getLogger('botocore.vendored.requests.packages.urllib3').level = logging.WARN
producer = KinesisProducer('borgstrom-test')

# for idx in range(100):
#     producer.put(str(idx))


#Self-explanatory, I hope
class Main():

    done = False

    def __init__(self):
        
        pygame.init()


        #Gets and initializes any controllers plugged in. May break stuff if a non-360 controller
            #is plugged in
        self.joysticks = []
        
        for i in range(0, pygame.joystick.get_count()):
                self.joysticks.append(pygame.joystick.Joystick(i))
                self.joysticks[-1].init()
                print ("Detected joystick '",self.joysticks[-1].get_name(),"'")


    def main_loop(self):
        while not self.done:
            self.handle_events()
        pygame.quit()



    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = Truemsg


            elif event.type == JOYBUTTONDOWN:
                gh_event = {
                    "type": JOYBUTTONDOWN,
                    "button": event.button
                }

                msg = json.dumps(gh_event)
                print("v:", msg)
                
                # producer.put("v")
                producer.put(msg)

            elif event.type == JOYBUTTONUP:
                gh_event = {
                    "type": JOYBUTTONUP,
                    "button": event.button
                }

                msg = json.dumps(gh_event)
                print("v:", msg)
                                
                # producer.put("^")
                producer.put(msg)


if __name__ == '__main__':
    game = Main()
    game.main_loop()

