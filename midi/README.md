# MIDI

spec: https://www.midi.org/specifications/item/table-1-summary-of-midi-message

see: https://en.wikipedia.org/wiki/General_MIDI#Program_change_events


General Midi: https://jazz-soft.net/demo/GeneralMidi.html

## Python

music21: http://web.mit.edu/music21/

mido: https://mido.readthedocs.io/en/latest/index.html

## Control Change



https://www.midi.org/specifications/item/table-3-control-change-messages-data-bytes-2

## Example Dump

```
Track 0: 
<meta message set_tempo tempo=375000 time=0>
<meta message key_signature key='C' time=0>
<meta message time_signature numerator=4 denominator=4 clocks_per_click=24 notated_32nd_notes_per_beat=8 time=0>
<meta message end_of_track time=0>
Track 1: Untitled
control_change channel=0 control=0 value=0 time=0
control_change channel=0 control=32 value=0 time=0
program_change channel=0 program=42 time=0
<meta message track_name name='Untitled' time=0>
control_change channel=0 control=7 value=127 time=0
note_on channel=0 note=67 velocity=61 time=836
note_off channel=0 note=67 velocity=0 time=282


note_off channel=0 note=64 velocity=0 time=6
note_off channel=0 note=47 velocity=0 time=7
control_change channel=0 control=127 value=0 time=811
<meta message end_of_track time=0>

```

### Detail

Description | Message 
--- | --- | ---
Bank Select 0 (MSB)| `control_change channel=0 control=0 value=0 time=0` 
Bank Select 0 (LSB)| `control_change channel=0 control=32 value=0 time=0`
All Notes Off | `control_change channel=0 control=127 value=0 time=811`
Change Instrument to Cello (42)| `program_change channel=0 program=42 time=0`

## Meta

```
<meta message set_tempo tempo=375000 time=0>
<meta message key_signature key='C' time=0>
<meta message time_signature numerator=4 denominator=4 clocks_per_click=24 notated_32nd_notes_per_beat=8 time=0>
<meta message end_of_track time=0>

<meta message track_name name='Untitled' time=0>

```