import requests
import uuid

def create_presentation(access_token):
    url = "https://alai-standalone-backend.getalai.com/create-new-presentation"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "*/*"
    }

    payload = {
        "presentation_id": str(uuid.uuid4()),
        "presentation_title": "Untitled Presentation",
        "create_first_slide": True,
        "theme_id": "a6bff6e5-3afc-4336-830b-fbc710081012",
        "default_color_set_id": 0
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # print("Presentation created successfully!")
        # print("Presentation ID:", data["id"])
        return data
    else:
        # print("Failed to create presentation.")
        # print("Status code:", response.status_code)
        # print("Response:", response.text)
        return {}