from pyneuphonic import Neuphonic, AudioPlayer, TTSConfig
import asyncio

async def play_audio(text, gender):
    api_key = '8a27099524e3390cbeefd2975bdc2d2ee6d9bac1ae329407899c1c300f09008a.0be1bf4f-3463-462b-81ca-5e4e790f1494'  # Directly pass your API key here
    client = Neuphonic(api_key=api_key)
    sse = client.tts.SSEClient()
    # To edit the voice edit whats below
    male = TTSConfig(speed=1.2, voice='ebf2c88e-e69d-4eeb-9b9b-9f3a648787a5', temperature= 0.9)
    female =  TTSConfig(speed=1.05, voice='e564ba7e-aa8d-46a2-96a8-8dffedade48f')

    if gender.lower() == 'male':
        tts_config = male
    else:
        tts_config = female

    with AudioPlayer() as player:
        response = sse.send(text, tts_config=tts_config)

        for item in response:
            player.play(item.data.audio)

async def main():
    # You can now call `play_audio` with any text and gender you want
    while True:
        # Example input
        text = "Hello, this is a test message."
        gender = "male"  # This can be changed to 'female'

        # Call play_audio with the text and gender
        await play_audio(text, gender)

        # Exit condition (you can change this logic)
        break

if __name__ == '__main__':
    asyncio.run(main())


    