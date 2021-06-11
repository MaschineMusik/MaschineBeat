# SOX

### merge audio

```
sox -m in1.mp3 in2.mp3 in3.mp3 out.mp3
```

### mix and normalise

```
sox -m ex-piano.wav ex-cello.wav ex-mix.wav gain -n
```

### with relative volumes
```
sox -m -v 0.2 ex-piano.wav -v 1 ex-cello.wav ex-mix.wav gain -n
```