

    // local vars --------------------------


    var log = console.log.bind(console),
        keyData = document.getElementById('key_data'),
        midi;

    var statusMessage = document.getElementById('status_message');
    var waveform = document.getElementById('waveform');

    var AudioContext;
    var context;
    var btnBox = document.getElementById('content'),
        btn = document.getElementsByClassName('button');
    var data, cmd, channel, type, note, velocity;

    // request MIDI access -----------------

    navigator.requestMIDIAccess( { sysex: true } ).then( onMIDISuccess, onMIDIFailure );


    // if (navigator.requestMIDIAccess) {
    //     navigator.requestMIDIAccess({
    //         sysex: true
    //     }).then(onMIDISuccess, onMIDIFailure);
    // } else {
    //     alert("No MIDI support in your browser.");
    // }
    
    // add event listeners
    document.addEventListener('keydown', keyController);
    document.addEventListener('keyup', keyController);

    for (var i = 0; i < btn.length; i++) {
        btn[i].addEventListener('mousedown', clickPlayOn);
        btn[i].addEventListener('mouseup', clickPlayOff);
    }

    // prepare audio files
    for (var i = 0; i < btn.length; i++) {
        bindSound(btn[i]);
    }
    
    try {
        AudioContext = window.AudioContext || window.webkitAudioContext; // for ios/safari
        context = new AudioContext();
    }
    catch(e) {
      alert('Web Audio API is not supported in this browser');
    }

    updateStatus("READY");