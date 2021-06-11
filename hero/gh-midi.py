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


# for idx in range(100):
#     producer.put(str(idx))

port = mido.open_output() 

#notes = [80, 82, 87, 84, 89, 92, 94, 96, 98, 99]
notes = [56, 58, 63, 60, 65, 68, 70, 72, 74, 75]

#riff = [60, 62, 69, 64, 67, 72, 60, 60, 60, 60]
riff = [60, 62, 67, 64, 69, 72, 6, 7, 8, 9]

notes = riff # [0,1,2,3,4,5,6,7,8,9] # riff

# GH 0 1 3 2 4 5 

# PG 0 1 2 5 6 7
#notes = [0, 1, 5, 2, 6, 7, 3, 3, 4, 4]

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

            # print(event)

            if event.type == pygame.QUIT:
                self.done = True


            elif event.type == JOYBUTTONDOWN:
                note=notes[event.button]
                print("v ", note)
                on = Message('note_on', note=note)
                port.send(on)

            elif event.type == JOYBUTTONUP:
                note=notes[event.button]
                print("^ ", note)
                off = Message('note_off', note=note)
                port.send(off)


            elif event.type == JOYHATMOTION:
                hat = event.hat
                value = event.value
                print(value)

            elif event.type == JOYAXISMOTION:
                axis = event.axis

            else:
                print(event)

if __name__ == '__main__':
    game = Main()
    game.main_loop()

