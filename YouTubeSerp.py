import requests
import json
import base64

# Replace 'your_login' and 'your_password' with your actual DataForSEO API login and password
login = "tjnfinancial@protonmail.com"
password = "3cce0092b625d73c"

def get_youtube_serp_video_info(language_code, location_code, video_id):
    api_url = "https://api.dataforseo.com/v3/serp/youtube/video_info/live/advanced"
    cred = base64.b64encode(f"{login}:{password}".encode()).decode()

    headers = {
        "Authorization": f"Basic {cred}",
        "Content-Type": "application/json"
    }

    data = [
        {
            "language_code": language_code,
            "location_code": location_code,
            "video_id": video_id
        }
    ]

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

if __name__ == "__main__":
    language_code = input("Enter the search engine language code (e.g., 'en'): ")
    location_code = int(input("Enter the search engine location code (e.g., 2840): "))
    video_id = input("Enter the video ID: ")

    try:
        result = get_youtube_serp_video_info(language_code, location_code, video_id)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(str(e))
