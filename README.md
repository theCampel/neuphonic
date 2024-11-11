## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm (comes with Node.js)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env file with your API keys:
# - OPENAI_API_KEY
# - TTS_API_KEY

# Start the Flask server
python app.py
```

The backend server will start at `http://localhost:5000`

### 3. Frontend Setup

```bash
# Open a new terminal
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

The frontend will open automatically at `http://localhost:3000`

## Usage

1. Open your browser to `http://localhost:3000`
2. Click the "Play" button
3. The application will:
   - Generate text using ChatGPT
   - Convert the text to speech
   - Stream the audio to your browser

## Environment Variables

The following environment variables need to be set in `backend/.env`:

- `OPENAI_API_KEY`: Your OpenAI API key
- `TTS_API_KEY`: Your Text-to-Speech service API key

## Development

- Backend code is in the `backend/` directory
- Frontend code is in the `frontend/` directory
- API services are in `backend/services/`

## Troubleshooting

1. If you get a "Module not found" error:
   - Make sure you've activated the virtual environment
   - Verify all dependencies are installed

2. If the frontend can't connect to the backend:
   - Ensure the backend server is running
   - Check that you're using the correct ports

3. If API calls fail:
   - Verify your API keys in the `.env` file
   - Check the backend console for error messages

