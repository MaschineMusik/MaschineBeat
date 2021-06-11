.PHONY:  docker


# make -e MIDI=mary INI=Chill compose
# make -e CONFIG=space MIDI=mary INI=Space new

MIDI = hero
MIDI = entertainer

INI  = Space
CONFIG = space
MIDI = mary

# UTILS -----------

STATUS = ../midi/sysex.py
READY = 0
RECORDING = 1
COMPOSING = 2
ARRANGING = 3
MIXING = 4

docker:
	docker build -t flow:latest .

explain:
	# docker-compose run --rm flow python explain.py config.yaml
	python explain.py config/config.$(CONFIG).yaml

shell:
	docker-compose run --rm flow bash

dump:
	python ../midi/dump.py config/Midi/$(MIDI).mid 

ready:
	$(STATUS) $(READY)

# THE REAL STUFF -----------



capture:
	arecordmidi -p 0 -b 180 config/Midi/$(MIDI).mid

compose:
	$(STATUS) $(COMPOSING)
	docker-compose run --rm beat python wbDev.py -m Midi/$(MIDI).mid  -i Ini/$(INI).ini
	echo "COMPOSED"

arrange:
	$(STATUS) $(ARRANGING)
	rm -rf output/arrange/*
	# docker-compose run --rm flow python arrange.py output/compose output/arrange
	python arrange.py config/config.$(CONFIG).yaml output/compose output/arrange
	echo "ARRANGED"

record:
	rm -rf output/record/*
	#docker-compose run --rm flow bash record.sh
	./record.sh config/config.$(CONFIG).yaml
	echo "RECORDED"

record_merged:
	fluidsynth -i \
        -F output/mix/merged.wav \
        -g 5.0 \
        FluidR3_GM.sf2 \
        output/arrange/merged.mid
	echo "RECORDED"

mix:
	$(STATUS) $(MIXING)
	rm -rf output/mix/*
	#docker-compose run --rm flow bash mix.sh
	./mix.sh config/config.$(CONFIG).yaml
	echo "MIXED"

master:
	rm -rf output/master/*
	#docker-compose run --rm flow bash mix.sh
	./master.sh config/config.$(CONFIG).yaml
	echo "MASTERED"
	$(STATUS) $(READY)

# OTHER STUFF --------------------------

demo: capture new play
	echo "DEMO"
	
play:
	play output/master/master.wav

new: compose arrange record mix master
	echo "NEW"

rearrange: arrange record mix master
	echo "RE-ARRANGED"

remix: mix master
	echo "RE-MIXED"

clean:
	rm -rf output/compose/*
	rm -rf output/arrange/*
	rm -rf output/record/*
	rm -rf output/mix/*
	rm -rf output/master/*

dirs:
	mkdir -p output
	mkdir -p output/compose
	mkdir -p output/arrange
	mkdir -p output/record
	mkdir -p output/mix
	mkdir -p output/master

