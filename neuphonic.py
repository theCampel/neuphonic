from pyneuphonic import Neuphonic, AudioPlayer
import asyncio
import aioconsole

async def main():
    api_key = 'my_api_key'  # Directly pass your API key here
    client = Neuphonic(api_key=api_key)
    sse = client.tts.SSEClient()

    with AudioPlayer() as player:
        while True:
            user_text = await aioconsole.ainput(
                "Enter text to speak (or 'quit' to exit): "
            )

            if user_text.lower() == 'quit':
                break

            response = sse.send(user_text)

            for item in response:
                player.play(item.data.audio)

if __name__ == '__main__':
    asyncio.run(main())
