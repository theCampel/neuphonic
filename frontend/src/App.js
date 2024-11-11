import React, { useState } from 'react';
import AudioPlayer from './components/AudioPlayer';
import { generateText } from './services/api';
import './index.css';

function App() {
  const [isPlaying, setIsPlaying] = useState(false);

  const handlePlay = async () => {
    setIsPlaying(true);
    try {
      const text = await generateText();
      // Initialize WebSocket connection for TTS streaming
      const socket = new WebSocket('ws://localhost:5000');
      
      socket.onopen = () => {
        socket.send(JSON.stringify({ type: 'start_tts', text }));
      };
      
    } catch (error) {
      console.error('Error:', error);
      setIsPlaying(false);
    }
  };

  const handleStop = () => {
    setIsPlaying(false);
    // Placeholder function for stop functionality
    console.log('Stop button clicked');
    // You might want to:
    // 1. Close WebSocket connection
    // 2. Stop audio playback
    // 3. Reset any relevant state
  };

  return (
    <div className="App">
      <div className="button-container">
        <button 
          onClick={handlePlay}
          disabled={isPlaying}
          className="play-button"
        >
          {isPlaying ? 'Playing...' : 'Play'}
        </button>
        <button 
          onClick={handleStop}
          disabled={!isPlaying}
          className="stop-button"
        >
          Stop
        </button>
      </div>
      <AudioPlayer isPlaying={isPlaying} />
    </div>
  );
}

export default App; 