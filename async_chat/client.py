import asyncio
import websockets


async def chat_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server...")
        name = input("Welcome :)\nSet a nickname: ")
        await websocket.send(f"{name} joined chat")

        try:
            while True:
                msg = input(f"{name}: ")
                await websocket.send(f"{name}: {msg}")

                response = await websocket.recv()
                print(response)
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed.")


asyncio.run(chat_client())
