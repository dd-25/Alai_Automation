import requests

def scrape_url(url):
    FIRECRAWL_API_KEY = 'your-api-key'
    headers = {
    'Authorization': f'Bearer {FIRECRAWL_API_KEY}',
    'Content-Type': 'application/json'
    }
    endpoint = 'https://api.firecrawl.dev/v1/scrape'
    payload = {
    'url': url
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        # print("Full Response Structure:\n")
        # print(data)  # Print entire structure to find where content is
        return data
    else:
        # print("Failed to fetch data. Status Code:", response.status_code)
        # print(response.text)
        return None