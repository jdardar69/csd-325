# astros_api.py
# Jordan Dardar
# Module 9.2 Assignment: APIs - Astronauts Tutorial Program

import requests

def main():
    # 1. Test the connection to the API
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    print("Connection test (status code):")
    print(response.status_code)      # 200 means OK
    print("-" * 40)

    # 2. Print raw response (no formatting)
    print("Raw response text from the API:")
    print(response.text)             # this is just big JSON text
    print("-" * 40)

    # 3. Print formatted output
    data = response.json()           # turn JSON text into a Python dict

    print("Formatted output:")
    print(f"Number of people in space: {data['number']}")
    print()

    for person in data["people"]:
        name = person["name"]
        craft = person["craft"]
        print(f"{name} is aboard {craft}.")

if __name__ == "__main__":
    main()
