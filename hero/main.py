
from __future__ import print_function
import sys
import os
import time
import random
import mido

import pygame

from mido import Message
from pygame.locals import *


REC_START = 1
REC_STOP  = 2


#Self-explanatory, I hope
class Main():

    done = False
    capture = False
    port = False

    # A pentatonic scale [first 6 ] + start(1) - stop(2) - xx() - xx()
    notes = [60, 62, 67, 64, 69, 72, REC_START, REC_STOP, 0, 0]

    def __init__(self):
        
        pygame.init()


        #Gets and initializes any controllers plugged in. May break stuff if a non-360 controller
            #is plugged in
        self.joysticks = []
        
        for i in range(0, pygame.joystick.get_count()):
                self.joysticks.append(pygame.joystick.Joystick(i))
                self.joysticks[-1].init()
                print ("Detected joystick '",self.joysticks[-1].get_name(),"'")

        self.local = mido.open_output('Midi Through:Midi Through Port-0 14:0') 

    def main_loop(self):
        while not self.done:
            self.handle_events()
        pygame.quit()

    def noteOn(self, button):
        on = Message('note_on', note=self.notes[button])

        self.local.send(on)
        
        if (self.capture) & (button <= 5) :
            self.port.send(on)


    def noteOff(self, button):
        off = Message('note_off', note=self.notes[button])
        self.local.send(off)

        if (self.capture) & (button <= 5) :
            self.port.send(off)


    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            # print(event)

            if event.type == pygame.QUIT:
                self.done = True


            #Controller controls
            elif event.type == JOYBUTTONDOWN:

                button = event.button

                print("v:", button )

                if (button == 9) & (self.capture == False):
                    print("START")
                    self.capture = True
                    os.system("arecordmidi -p 0 -b 180 ../flow/config/Midi/hero.mid &")
                    time.sleep(1)
                    self.port = mido.open_output('arecordmidi:arecordmidi port 0')
                    self.local.send(Message('note_on', note=REC_START))
                elif (button == 6) & (self.capture == True):
                    print("STOP")
                    self.capture = False
                    self.local.send((Message('note_on', note=REC_STOP)))
                    os.system("pkill -SIGINT arecordmidi")
                    os.system("cd ../flow && make new")
                    # exit
                elif (button <= 5):
                    self.noteOn(button)

            elif event.type == JOYBUTTONUP:
                button = event.button
                print("^:", button )

                if (button <= 5):
                    self.noteOff(button)

            elif event.type == JOYHATMOTION:
                print("-:", event.value )


if __name__ == '__main__':

    print("MIDI ports:", mido.get_output_names())
    game = Main()
    game.main_loop()

