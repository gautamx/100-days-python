# The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. 
# This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
import requests

response = requests.get("https://www.google.com")
# print(response.text)

from bs4 import BeautifulSoup             # bs4 module for webscraping

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)

###############################################################################################################################

import requests

# GET Request
response = requests.get('https://api.example.com/users')
print(response.status_code)  # HTTP status code
print(response.text)         # Response content as text
print(response.json())       # Parse JSON response

# POST Request
data = {'username': 'john', 'password': 'secret'}
response = requests.post('https://api.example.com/login', json=data)

# Different HTTP methods
requests.get(url)     # Retrieve data
requests.post(url)    # Submit data
requests.put(url)     # Update data
requests.delete(url)  # Delete data
requests.patch(url)   # Partial update

# Query parameters
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api.example.com/search', params=payload)

# Custom headers
headers = {
    'User-Agent': 'My User Agent 1.0',
    'Authorization': 'Bearer token123'
}
response = requests.get(url, headers=headers)

response = requests.get(url)

# Check status
print(response.status_code)
print(response.ok)  # True if status code < 400

# Response content
print(response.text)        # Text content
print(response.content)     # Raw bytes
print(response.json())      # JSON parsing

# Headers
print(response.headers)
print(response.headers['Content-Type'])

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Different exception types
requests.exceptions.ConnectionError    # Network problems
requests.exceptions.Timeout            # Timeout errors
requests.exceptions.HTTPError          # HTTP error responses

# Basic Authentication
response = requests.get(url, auth=('username', 'password'))

# Bearer Token
headers = {'Authorization': 'Bearer token123'}
response = requests.get(url, headers=headers)

# Uploading a file
files = {'file': open('report.pdf', 'rb')}
response = requests.post(url, files=files)

# Multiple files
files = {
    'file1': open('doc1.txt', 'rb'),
    'file2': open('doc2.txt', 'rb')
}

# Persistent session
session = requests.Session()
session.get('https://example.com/login')
session.post('https://example.com/profile')

# Cookies
response = requests.get(url)
print(response.cookies)

# Set connection and read timeouts
try:
    response = requests.get(url, timeout=(3.05, 27))
except requests.exceptions.Timeout:
    print("The request timed out")

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}
response = requests.get(url, proxies=proxies)

#################################################################################################################################

import requests

def fetch_user_data(user_id):
    """
    Fetch user data from an API
    
    Args:
        user_id (int): ID of the user to fetch
    
    Returns:
        dict: User data or None if error
    """
    try:
        # API endpoint
        url = f'https://api.example.com/users/{user_id}'
        
        # Headers
        headers = {
            'User-Agent': 'MyApp/1.0',
            'Accept': 'application/json'
        }
        
        # Make the request
        response = requests.get(url, headers=headers, timeout=5)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Return JSON data
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        return None

# Usage
user_data = fetch_user_data(123)
if user_data:
    print(user_data)