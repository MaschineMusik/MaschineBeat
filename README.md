# MaschineBeat
Automated pipeline for music creation using IBM Watson Beat

## TODO

1. decouple instrument from midi file - use fluid synth [does not seem possible]
2. config files for orchestra


## yaml

```
orchestra:
  - soundfonts: 
        name: FluidR3_GM.sf2
        - bank: 0

tracks:
   name: piano
   - soundfont: 
   - program: 1 # grand piano
   - volume: 0.9
   - pan: -0.4

```