# Pyina

## General Info
Windows has GINA to keep track of many different spells and events. As a Linux user
I was looking for something to help keep track of spell durations. I could not find one
so I tossed together a makeshift GINA in python.

Pyina will search the EQ log file for a spell you want to track and start a timer. 
As of now it will only track one spell at a time. I hope to add more features in
the future.

To track more than on spell at a time just make copies of pyina and rename it.
for instance you can copy and rename to pyina_fear.py or pyian_snare.py etc.

## Installation
* Python 3 required
* Copy pyina.py to any location
* Configure pyina.py in the Set Up section of the file
* Use your favorite editor to edit
* Use python3 to run

'''
$ python3 pyina.py
'''

## Set Up Section
*  LOGFILE:  The log file location in the Everquest directory
*  SPELL_NAME: The name of the spell you are tracking
*  SPELL_TEXT: The spell text to search for in the log file
*  SPELL_TIME: The duration of the spell in seconds

### Set Up Section Example

'''
23 LOGFILE = "/home/home_dir/.wine/drive_c/Program Files (x86)/Sony/EverQuest/Logs/eqlog_Ch
28 SPELL_NAME = "Fear Timer"                                                       
29 SPELL_TEXT = "looks very afraid"                                                
30 SPELL_TIME =  42                                                                
'''

