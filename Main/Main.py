# 01/03/2023
# Author: Del161

import mido
import sys
import RaspberryFPPlayer as RFPP

def importfile(song):
    # simply opens the file

    #current placeholder will be replaced with sys.argv
    mid = mido.MidiFile(song, clip=True)
    tracks = mid.tracks

    return tracks
    

def extractdata(tracks, u_track):
    x = 0
    # you would want the track with the not_on and note_off messages
    # these will be the main notes most often
    # you can use this to check
    #for t in tracks:
    #    for message in t[0:20]:
    #        print(message)
    #    print("###########################")

    fulltrack =[]

    # have to make it into a list so its a usable type
    for messages in tracks[u_track]:
        if str(messages).startswith("note"):
            fulltrack.append(str(messages)) 
    for lines in fulltrack:
        lines = lines.split(" ")
        print(lines)





def main():
    # main

    # allows the user to input what song and track they want
    arguments = sys.argv
    if len(arguments)>1:
        song = arguments[1]
    else: song = "../Samplemusic/OCaraMia.mid"
    if len(arguments)>2:
        u_track = arguments[2]
    else: u_track = 3

    tracks = importfile(song)
    extractdata(tracks, u_track)
    RFPP.setup()
    RFPP.reset()
    RFPP.calculate_pause()

if __name__ == "__main__":
    main()