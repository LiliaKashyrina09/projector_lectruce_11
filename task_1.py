import requests

def search_gifs(query):
    api_key = "U7mNfnGLCeG123CyjmdArb0tfR9Z9Jbk"  
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": query,
        "limit": 3  
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    for gif in data['data']:
        print(gif['images']['original']['url'])


search_term = input("Enter a search term for a GIF: ")
search_gifs(search_term)
