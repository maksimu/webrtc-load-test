import asyncio
import websockets
import json

connected = set()

async def echo(websocket, path):
    print("A client just connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected.remove(websocket)

start_server = websockets.serve(echo, "localhost", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
print("Signaling Server running on ws://localhost:5678")
asyncio.get_event_loop().run_forever()
