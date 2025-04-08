import asyncio
import websockets
import json
from websockets.client import connect

async def send_payload(access_token, presentation_id, scraped_data, slide_id, generate_slides_response):
    uri = "wss://alai-standalone-backend.getalai.com/ws/create-slides-from-outlines"
    payload = {
    "auth_token": access_token,
    "presentation_id": presentation_id,
    "presentation_instructions": "Create a professional presentatioin of 2 to 5 slides with visually appealing interface and in points don't write much text, also try to use images and consistent formatting",
    "raw_context": scraped_data,
    "slide_id": slide_id,
    "slide_outlines": [generate_slides_response],
    "starting_slide_order": 0,
    "update_tone_verbosity_calibration_status": True,
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

def run_slides_websocket(access_token, presentation_id, scraped_data, slide_id, generate_slides_response):
    return asyncio.run(send_payload(access_token, presentation_id, scraped_data, slide_id, generate_slides_response))