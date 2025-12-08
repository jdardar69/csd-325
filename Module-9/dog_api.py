# dog_api.py
# Jordan Dardar
# Module 9.2 Assignment: APIs - Custom API Program (Dog API)

import requests

def main():
    # 1. Test the connection to the API
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    print("Connection test (status code):")
    print(response.status_code)   # 200 = success
    print("-" * 40)

    # 2. Print raw response (no formatting)
    print("Raw response text from the API:")
    print(response.text)
    print("-" * 40)

    # 3. Print formatted output
    data = response.json()

    dog_image_url = data.get("message")
    status = data.get("status")

    print("Formatted output:")
    print(f"API Status: {status}")
    print(f"Random Dog Image URL: {dog_image_url}")

if __name__ == "__main__":
    main()
