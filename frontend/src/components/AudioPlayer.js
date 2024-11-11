import React, { useEffect, useRef } from 'react';

const AudioPlayer = ({ isPlaying }) => {
  const audioContext = useRef(null);
  const socket = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      // Initialize audio context
      audioContext.current = new (window.AudioContext || window.webkitAudioContext)();
      
      // Setup WebSocket connection
      socket.current = new WebSocket('ws://localhost:5000');
      
      socket.current.onmessage = (event) => {
        const audioData = JSON.parse(event.data);
        // Process audio chunk and play it
        // This is a placeholder - you'll need to implement actual audio processing
        console.log('Received audio chunk:', audioData);
      };
    }

    return () => {
      if (socket.current) {
        socket.current.close();
      }
    };
  }, [isPlaying]);

  return (
    <div>
      {isPlaying && <div>Audio is playing...</div>}
    </div>
  );
};

export default AudioPlayer; 