# 01/03/2023
# Author: Del161

import mido

def importfile():
    # simply opens the file

    mid = mido.MidiFile("../Samplemusic/?.midi", clip=True)
    tracks = mid.tracks

    return tracks
    


def extractdata(tracks):
    x = 0
    for t in tracks:
        for message in t[0:20]:
            print(message)
        print("###########################")


def main():
    tracks = importfile()
    extractdata(tracks)

if __name__ == "__main__":
    main()