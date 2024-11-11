from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from services.chatgpt_service import generate_text
from services.tts_service import text_to_speech
from config import Config

# Validate environment variables before starting the app
Config.validate_config()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/api/generate', methods=['POST'])
def generate():
    # Placeholder endpoint that will trigger the ChatGPT API
    text = generate_text()
    return jsonify({"text": text})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('start_tts')
def handle_tts(data):
    text = data.get('text', '')
    # Start streaming TTS audio
    for audio_chunk in text_to_speech(text):
        emit('audio_chunk', {'data': audio_chunk})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000) 