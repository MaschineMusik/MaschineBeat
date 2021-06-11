
import mido
import time

from mido import MidiFile, MidiTrack, Message


ticks_per_beat=480


mid = MidiFile(ticks_per_beat=self.ticks_per_beat)
track = MidiTrack()
mid.tracks.append(track)

elapsed = 0

with mido.open_input() as inport:
    for msg in inport:
        print(msg)
        if msg.note == 0:
            break
        track.append(msg)


print("STOP")
mid.save('new_song.mid')         