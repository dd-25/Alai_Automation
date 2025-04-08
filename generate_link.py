import requests

def generate_link(access_token, presentation_id):
    url = "https://alai-standalone-backend.getalai.com/upsert-presentation-share"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "*/*"
    }

    payload = {
        "presentation_id": presentation_id,
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # print("Access token retrieved successfully!")
        return data
    else:
        return {}