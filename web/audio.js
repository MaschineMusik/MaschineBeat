

function getSoundUrl(soundNo) {
    return(soundsPrefix + sounds[soundNo])
}

function loadSound(object, soundNo) {
    var request = new XMLHttpRequest();
    var url = getSoundUrl(soundNo);

    request.open('GET', url, true);
    request.responseType = 'arraybuffer';

    request.onload = function () {
        context.decodeAudioData(request.response, function (buffer) {
            object.buffer = buffer;
        });
    }
    request.send();
}

function bindSound(object) {
    object.name = object.id;
    loadSound(object, object.dataset.sound);

    object.play = function (volume) {
        var s = context.createBufferSource();
        var g = context.createGain();
        var v;
        s.buffer = object.buffer;
        s.playbackRate.value = 1.0 // randomRange(0.5, 2);
        if (volume) {
            v = rangeMap(volume, 1, 127, 0.2, 2);
            s.connect(g);
            g.gain.value = v * v;
            g.connect(context.destination);
        } else {
            s.connect(context.destination);
        }

        s.start();
        object.s = s;
    }
}
