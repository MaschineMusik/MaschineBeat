// config vars -------------


// this maps the MIDI key value (60 - 64) to our samples
// pentatonic 60, 62, 64, 67, 69, 72

var sampleMap = {
    key60: 1,
    key62: 3,
    key64: 5,
    key67: 2,
    key69: 4,
    key72: 6
};

// keyboard map ASCII => button #

var keyMap = {
    65: 0, // a
    83: 2, // s
    68: 4, // d
    81: 1, // q
    87: 3, // w
    69: 5 // e
};

// user interaction, mouse click
function clickPlayOn(e) {
    e.target.classList.add('active');
    e.target.play();
}

function clickPlayOff(e) {
    e.target.classList.remove('active');
}
// qwerty keyboard controls. [q,w,e,r,t,y]
function keyController(e) {
    if (e.type == "keydown") {

        buttonNo = keyMap[e.keyCode];
        console.log(buttonNo);

        btn[buttonNo].classList.add('active');
        btn[buttonNo].play();      

    } else if (e.type == "keyup") {

        buttonNo = keyMap[e.keyCode];
        console.log(buttonNo);

        btn[buttonNo].classList.remove('active');
    }
}

// midi functions
function onMIDISuccess(midiAccess) {
    midi = midiAccess;
    var inputs = midi.inputs.values();
    // loop through all inputs
    for (var input = inputs.next(); input && !input.done; input = inputs.next()) {
        // listen for midi messages
        input.value.onmidimessage = onMIDIMessage;
        // this just lists our inputs in the console
        listInputs(input);
    }
    // listen for connect/disconnect message
    midi.onstatechange = onStateChange;
}

function onMIDIMessage(event) {
    var data = event.data;

    console.log('MIDI data', data);

    // with pressure and tilt off
    // note off: 128, cmd: 8 
    // note on: 144, cmd: 9
    // pressure / tilt on
    // pressure: 176, cmd 11: 
    // bend: 224, cmd: 14

    if (data[0] < 240) {

        var cmd = data[0] >> 4,
            channel = data[0] & 0xf,
            type = data[0] & 0xf0, // channel agnostic message type. Thanks, Phil Burk.
            note = data[1],
            velocity = data[2];

        switch (type) {
            case 144: // noteOn message 
                logger(keyData, 'key data', data);
                noteOn(note, velocity);
                break;
            case 128: // noteOff message 
                logger(keyData, 'key data', data);
                noteOff(note, velocity);
                break;
            case 176: // controlChange message 
                controlChange(data[1], data[2]);
                break;
        }

        console.log('data', data, 'cmd', cmd, 'channel', channel, 'type', type);
    }
    else
    if (data[0] == 240) {
        sysex(data[1]);
    }
    else {
        console.log('UNKNOWN MIDI Event', data);
    }

}

function onStateChange(event) {
    var port = event.port,
        state = port.state,
        name = port.name,
        type = port.type;
    if (type == "input") console.log("name", name, "port", port, "state", state);
}

function listInputs(inputs) {
    var input = inputs.value;
    log("Input port : [ type:'" + input.type + "' id: '" + input.id +
        "' manufacturer: '" + input.manufacturer + "' name: '" + input.name +
        "' version: '" + input.version + "']");
}


function controlChange(control, value) {
    keyData.textContent = "controlChange: " + control + " = " + value;;
}

function sysex(code) {
    console.log('sysex', code);
    keyData.textContent = "sysex: " + code;

    switch (code) {
    // handle special control messages
        case 0: // reset
            updateStatus("READY");

            // force cache reload
            fetch("/media/master/master.wav", {cache: "reload", credentials: "include"});

            wavesurfer.load('./media/master/master.wav');
            wavesurfer.play();
            break;

        case 1: // start
            wavesurfer.empty();
            updateStatus("RECORDING");
            break;

        case 2:// composing
            wavesurfer.empty();
            updateStatus("COMPOSING");
            break;

        case 3: // arranging
            updateStatus("ARRANGING");
            break;

        case 4: // mixing
            updateStatus("MIXING");
            break;
    }
}

function noteOn(midiNote, velocity) {
    player(midiNote, velocity);
}

function noteOff(midiNote, velocity) {
    player(midiNote, velocity);
}

function player(note, velocity) {
    var sample = sampleMap['key' + note];
    if (sample) {
        if (type == (0x80 & 0xf0) || velocity == 0) { //QuNexus always returns 144
            btn[sample - 1].classList.remove('active');
            return;
        }
        btn[sample - 1].classList.add('active');
        btn[sample - 1].play(velocity);
    }
}

function onMIDIFailure(e) {
    log("No access to MIDI devices or your browser doesn't support WebMIDI API. Please use WebMIDIAPIShim " + e);
}


// utility functions
function randomRange(min, max) {
    return Math.random() * (max + min) + min;
}

function rangeMap(x, a1, a2, b1, b2) {
    return ((x - a1) / (a2 - a1)) * (b2 - b1) + b1;
}

function frequencyFromNoteNumber(note) {
    return 440 * Math.pow(2, (note - 69) / 12);
}

function logger(container, label, data) {
    messages = label + " [channel: " + (data[0] & 0xf) + ", cmd: " + (data[0] >> 4) + ", type: " + (data[0] & 0xf0) + " , note: " + data[1] + " , velocity: " + data[2] + "]";
    container.textContent = messages;
}

function updateStatus(status) {
    statusMessage.textContent = status;
}


function XonMIDIMessage(event) {
    var str = "MIDI message received at timestamp " + event.timestamp + "[" + event.data.length + " bytes]: ";
    for (var i = 0; i < event.data.length; i++) {
        str += "0x" + event.data[i].toString(16) + " ";
    }
    console.log(str);
}
