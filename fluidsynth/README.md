
## docker

```
docker build -t fluidsynth:latest .

docker-compose run fs
```


## examples

```
fluidsynth -F example.wav /usr/share/sounds/sf2/FluidR3_GM.sf2 example.mid

```

```
fluidsynth -i -f config -F ex-piano.wav -g 5.0 FluidR3_GM.sf2 ex-piano.mid

fluidsynth -i -f config -F ex-cello.wav -g 5.0 /usr/share/sounds/sf2/FluidR3_GM.sf2 ex-cello.mid 
```