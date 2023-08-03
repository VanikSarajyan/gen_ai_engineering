import asyncio
import websockets

connected_clients = set()


async def handle_message(message, sender):
    print(message)
    # Broadcast the message to all connected clients, excluding the sender
    for client in connected_clients:
        if client != sender:
            await client.send(message)


async def handle_client(websocket):
    # Add the client to the connected_clients set
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Handle incoming messages from the client
            await handle_message(message, websocket)
    finally:
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(
        handle_client, "localhost", 8765, ping_interval=None, ping_timeout=None
    )
    print("Server started...")
    await server.wait_closed()


asyncio.run(main())
