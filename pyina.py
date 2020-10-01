### Pyina created by Joe Burgess.
### Must use python3 to run.

### This program tracks a spell and starts a timer.
### When program opens right click and set to Stay on Top if you like.

#!/usr/bin/python3

# libraries some are not used.
import subprocess
import time
import sys
import os

from os import listdir
from os.path import isfile, join

from tkinter import *

############# Set Up Section. ##########################

### Required: Set the path to your log file here.
LOGFILE = "/home/home_dir/.wine/drive_c/Program Files (x86)/Sony/EverQuest/Logs/eqlog_CharName_project1999.txt"

### Optinal: SPELL_NAME - Sets the text in the GUI. 
### Required: SPELL_TEXT - Searches for the text in the log file. The example here is for fear. It searches the log file for "looks very afraid" ###
### Required: SPELL_TIME - Sets the duration of the spell in seconds.
SPELL_NAME = "Fear Timer"
SPELL_TEXT = "looks very afraid"
SPELL_TIME =  42

#######################################################################



############## NO NEED TO CHANGE THE CODE BELOW #################
################################################################

### Opens the log file and moves to the last line ###
f = open(LOGFILE, 'r')
f.seek(0,2)
print("Reading Log File")

root=Tk()

### Function to start the spell timer ###
def spell_timer(timer):
    while timer:
        ### Checks to see if spell was re-cast and restart timer ###
        line = f.readline()
        if SPELL_TEXT in line:
            root.after(50, spell_timer(SPELL_TIME))

        l2["text"] = timer
        root.update()
        time.sleep(1)
        timer -= 1
    else:
        l2["text"] = "Times up!"                    
        root.after(0, read_log)    
        

### Funcion to Loop over log file and search for spell cast ###
def read_log():
    line = f.readline()
    if SPELL_TEXT in line:
        spell_timer(SPELL_TIME)    
        root.after(50, read_log)
    else:
        root.after(50, read_log)

### Closes the log file and exits program ###
def exit_prog():
    f.close()
    root.quit()              
    print("Closing log file and exiting")

### Widgets and layout for GUI ###
root.geometry("230x155")
root.title("Pyina")
l1=Label(root,font="times 20",text=SPELL_NAME)
l1.pack()
l2=Label(root, font="times 15", text = "0")
l2.pack()
btn1=Button(root, text="Exit", command = exit_prog)
btn1.pack()

### Starts the program.###
root.after(50, read_log)

root.mainloop()

