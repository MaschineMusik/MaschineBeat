import sys

from mido import MidiFile


def main(filename):

    mid = MidiFile(filename)

    # for i, track in enumerate(mid.tracks):
    #     print('Track {}: {}'.format(i, track.name))
    #     for msg in track:
    #         print(msg)

    for msg in mid:
        # if msg.type == 'program_change':
            print(msg)


if __name__ == '__main__':
    filename = sys.argv[1]  
    main(filename)  

    
