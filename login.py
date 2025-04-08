import requests

def get_access_token(email, password):
    url = "https://api.getalai.com/auth/v1/token?grant_type=password"
    
    headers = {
        "Content-Type": "application/json",
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzY2hvdHRoamdsamJ4amVyY3puIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTAxMTI0NzYsImV4cCI6MjAyNTY4ODQ3Nn0.3pZ7fQ9qWjBcX-oSLJ37P4D9ojrdTF1zdI1B4ONcxrE",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzY2hvdHRoamdsamJ4amVyY3puIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTAxMTI0NzYsImV4cCI6MjAyNTY4ODQ3Nn0.3pZ7fQ9qWjBcX-oSLJ37P4D9ojrdTF1zdI1B4ONcxrE"
    }

    payload = {
        "email": email,
        "password": password,
        "gotrue_meta_security": {}
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        access_token = data.get("access_token")
        # print("Access token retrieved successfully!")
        return access_token
    else:
        # print(f"Failed to login. Status code: {response.status_code}")
        # print(response.text)
        return {}

# # --- USAGE ---
# email = "sarveshbajaj804@gmail.com"
# password = "BFVEV4TS9cHqDA3"

# access_token = get_access_token(email, password)

# if access_token:
#     print("Access Token:\n", access_token)