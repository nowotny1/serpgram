import requests
import json
import base64

url = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"

# Replace 'login' and 'password' with your credentials from https://app.dataforseo.com/api-dashboard
login = "tjnfinancial@protonmail.com"
password = "3cce0092b625d73c"

credentials = f"{login}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/json"
}

# User input for desired prompts
language_code = input("Enter the language code: ")
location_code = int(input("Enter the location code: "))
keyword = input("Enter the keyword: ")
calculate_rectangles = input("Calculate rectangles? Enter 'true' or 'false': ").lower() == 'true'

data = [
    {
        "language_code": language_code,
        "location_code": location_code,
        "keyword": keyword,
        "calculate_rectangles": calculate_rectangles
    }
]

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    api_data = response.json()
    print(json.dumps(api_data, indent=2))
else:
    print(f"Error: {response.status_code}")
