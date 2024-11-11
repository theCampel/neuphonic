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

  return (
    <div className="App">
      <button 
        onClick={handlePlay}
        disabled={isPlaying}
      >
        {isPlaying ? 'Playing...' : 'Play'}
      </button>
      <AudioPlayer isPlaying={isPlaying} />
    </div>
  );
}

export default App; 