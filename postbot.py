import requests
import json

# Set your Postman API key here
postman_api_key = 'YOUR_API_KEY'

# Set the endpoint URL you want to get suggestions for
endpoint_url = 'https://api.example.com/'

# Set the parameter name you want to get suggestions for
parameter_name = 'example_param'

# Set the number of suggestions you want to receive
num_suggestions = 5

# Build the request payload
payload = {
    'snippet': endpoint_url,
    'variableName': parameter_name,
    'suggestions': num_suggestions
}

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': postman_api_key
}

# Send the API request to Postman
response = requests.post(
    'https://api.getpostman.com/aiassistant/generate-suggestions',
    headers=headers,
    data=json.dumps(payload)
)

# Check if the API request was successful
if response.status_code == 200:
    # Parse the response JSON
    suggestions = json.loads(response.content)['suggestions']

    # Print the suggestions
    print(f"Top {num_suggestions} suggestions for '{parameter_name}' on '{endpoint_url}':")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
