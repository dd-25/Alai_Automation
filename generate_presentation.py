import requests
import json

def generate_presentations(access_token, run_slides_websocket_response, slide):
  url = "https://alai-standalone-backend.getalai.com/update-slide-entity"
  headers = {
      "Authorization": f"Bearer {access_token}",
      "accept": "*/*",
      "content-type": "application/json"
  }
  payload = {
        "presentation_id": run_slides_websocket_response["id"],
        "id": run_slides_websocket_response["id"],
        "slide_order": slide["slide_order"],
        "color_set_id": run_slides_websocket_response["default_color_set_id"],
        # "variants": slide["variants"],
        "created_at": run_slides_websocket_response["created_at"],
        "active_variant_id": slide["active_variant_id"],
        "slide_outline": slide["slide_outline"],
        "slide_status": slide["slide_status"],
        "images_on_slide": slide['slide_outline']["images_on_slide"],
    }
  response = requests.post(url, headers=headers, json=payload)

  if response.status_code == 200:
        # print("Slide updated successfully!")
        return response.json()
  else:
        # print("Failed to update slide:", response.status_code)
        # print(response.text)
        return {}

# Use the correct slide data
# first_slide = run_slides_websocket_response["slides"][0]
# presentation_id = run_slides_websocket_response["id"]

# generate_presentations_response = generate_presentations(access_token, first_slide)
# print(generate_presentations_response)