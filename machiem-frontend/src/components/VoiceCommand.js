import React, { useEffect } from 'react';

const VoiceCommand = ({ onCommand }) => {
    useEffect(() => {
        const recognition = new window.webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = (event) => {
            const transcript = Array.from(event.results)
                .map(result => result[0])
                .map(result => result.transcript)
                .join('');
            onCommand(transcript);
        };

        recognition.start();
    }, [onCommand]);

    return <div>Listening for commands...</div>;
};

export default VoiceCommand;
