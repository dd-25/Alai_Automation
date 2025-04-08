import asyncio
import websockets
import json
from websockets.client import connect

async def send_payload(access_token, presentation_id, scraped_data):
    uri = "wss://alai-standalone-backend.getalai.com/ws/generate-slides-outline"
    payload = {
    "auth_token": access_token,
    "presentation_id": presentation_id,
    "slide_order": 0,
    "raw_context": scraped_data,
    "presentation_instructions": "Create a professional presentatioin of 2 to 5 slides with visually appealing interface and in points don't write much text, also try to use images and consistent formatting",
    "slide_range": "2-5",
}
    async with websockets.connect(uri) as websocket:
        # print("Connected to Alai WebSocket")
        await websocket.send(json.dumps(payload))
        # print("Payload sent. Listening for messages...")

        try:
            while True:
                response = await asyncio.wait_for(websocket.recv(), timeout=30)
                # print(f"Received: {response}")
                return response
        except Exception as e:
            return {}

def run_websocket(access_token, presentation_id, scraped_data):
    return asyncio.run(send_payload(access_token, presentation_id, scraped_data))