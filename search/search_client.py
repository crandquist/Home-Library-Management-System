import requests
import json

def make_microservice_request(author, title):
    # Replace the URL with the actual URL of your partner's microservice
    microservice_url = "http://microservice-host:port/path"  

    # Create the request payload
    payload = {
        "author": author,
        "title": title
    }

    # Make a POST request to the microservice
    response = requests.post(microservice_url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle the case where the request was not successful
        print(f"Error: {response.status_code}")
        return None

# Example usage
author = "J.K. Rowling"
title = "Harry Potter"
response_data = make_microservice_request(author, title)

if response_data:
    # Process the response data as needed
    print(response_data)
