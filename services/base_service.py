import requests
BASE_URL = "http://jsonplaceholder.typicode.com"

#Get request API endpoint
def get(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    print("Response from GET request: ",response)
    response.raise_for_status() # Raises HTTPError for bad responses
    return response.json()

#Post request API endpoint
def post(endpoint, data):
    response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
    print("Response from POST request: ",response)
    response.raise_for_status() # Raises HTTPError for bad responses
    return response.json()

#Put request API endpoint
def put(endpoint, data):
    response = requests.put(f"{BASE_URL}/{endpoint}", json=data)
    print("Response from PUT request: ",response)
    response.raise_for_status() # Raises HTTPError for bad responses
    return response.json()    

#Delete request API endpoint
def delete(endpoint):
    response = requests.delete(f"{BASE_URL}/{endpoint}")
    print("Response from DELETE request: ",response)
    response.raise_for_status() # Raises HTTPError for bad responses
    return response.status_code