# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:01:00 2019

@author: pearlgod93
"""

import numpy as np
import scipy as sc
import rtmidi
import random

#Opening midi-output
midiout = rtmidi.MidiOut()
midiout.close_port()
midiout.open_port(0)
#Defining Morse code dictionary - For reference
MOR_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ',':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-','a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..', ' ': '+++'}

#getting input from the user
inputstr = input('Enter the string that needs to be generated as a song: ')

def convStr(inputString):
    morstring = ""
    for i in range(len(inputString)):
        morstring = morstring+MOR_DICT[inputString[i]]
    
    print(morstring)
    return morstring

def midi_play(note_val,time_val):

    #Note on definition
    note_on = [0x90, note_val, 127] # channel 1, middle C, velocity 112
    
    #Note off definition
    note_off = [0x80, note_val, 0] #note on corresponding note off  

    #Play chord
    midiout.send_message(note_on)
    time.sleep(time_val)
    midiout.send_message(note_off)

CMaj = (60,62,64,65,67,69,71,72,74,76,77,79,81,83,84)
DMaj = (62,64,66,67,69,71,73,74,76,78,79,81,83,85,86)
#inputString = "Hi Hello, and please listen"
morstring = convStr(inputstr)

for i in range(len(morstring)):
    if(morstring[i] == '.'):
       # print(random.choice(DMaj),'playing(.25)')
        midi_play(random.choice(DMaj),.25)
    elif(morstring[i] == '-'):
        #print(random.choice(DMaj),'playing(.5)')
        midi_play(random.choice(DMaj),.5)
    else:
        time.sleep(0.25)
    time.sleep(0.25)
midiout.close_port()
