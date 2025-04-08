from create_slides_from_outlines import run_slides_websocket
from generate_presentation import generate_presentations
from create_presentation import create_presentation
from generate_slides import run_websocket
from firecrawl_scraper import scrape_url
from generate_link import generate_link
from login import get_access_token
import json
import ast
import re

url = "your-url"
email = "your-email"
password = "your-password"

access_token = get_access_token(email, password)
scraped_data = scrape_url(url)
scraped_data = scraped_data['data']['markdown']
scraped_data = re.sub(r'\s+', ' ', scraped_data).strip()
scraped_data = scraped_data[:400000]

# print(access_token)
# print(scraped_data)

create_presentation_response = create_presentation(access_token)
# print(create_presentation_response)

generate_slides_response = run_websocket(access_token, create_presentation_response["id"], str(scraped_data))
# print(generate_slides_response)

generate_slides_response_dummy = generate_slides_response
if isinstance(generate_slides_response_dummy, str):
    generate_slides_response_dummy = json.loads(generate_slides_response_dummy)
run_slides_websocket_response = run_slides_websocket(access_token, create_presentation_response["id"], str(scraped_data), create_presentation_response['slides'][0]['id'], generate_slides_response_dummy)
# print(run_slides_websocket_response)

parsed_run_slides_websocket_response = run_slides_websocket_response
if isinstance(parsed_run_slides_websocket_response, str):
    try:
        parsed_run_slides_websocket_response = json.loads(parsed_run_slides_websocket_response)
    except json.JSONDecodeError:
        parsed_run_slides_websocket_response = ast.literal_eval(parsed_run_slides_websocket_response)
# print(parsed_run_slides_websocket_response)
# print(parsed_run_slides_websocket_response['slides'])
# print(parsed_run_slides_websocket_response.keys())
# print(type(parsed_run_slides_websocket_response['slides']))
slides = parsed_run_slides_websocket_response['slides']
for slide in slides:
    # we are facing issue in this part of the code
    generate_presentations_response = generate_presentations(access_token, parsed_run_slides_websocket_response, slide)
    # print(generate_presentations_response)

generate_link_response = generate_link(access_token, create_presentation_response["id"])
print(f"https://app.getalai.com/view/{generate_link_response}")