import requests
import json
import os
import yaml

def get_config():
    with open('_config.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def push_to_indexnow():
    config = get_config()
    indexnow_config = config.get('indexnow', {})
    
    if not indexnow_config.get('enabled', False):
        print("IndexNow is disabled in _config.yml")
        return

    site_url = config.get('url', '').rstrip('/')
    key = indexnow_config.get('key')
    key_location = indexnow_config.get('key_location')
    endpoint = indexnow_config.get('endpoint', 'https://api.indexnow.org/indexnow')

    if not key or not key_location:
        print("Error: IndexNow key or key_location is missing.")
        return

    # In a real scenario, you'd get the list of updated URLs.
    # Here, we'll push the main sitemap or recent posts as an example.
    # For Jekyll, we can read the _site/sitemap.xml or similar.
    
    # Simple example: push the home page and the last 10 posts
    # (Assuming we're running this after Jekyll build)
    
    urls_to_push = [f"{site_url}/"]
    
    # If _site exists, we could parse sitemap.xml
    # For this demo, let's just assume we want to push the home page.
    
    payload = {
        "host": site_url.replace('https://', '').replace('http://', ''),
        "key": key,
        "keyLocation": key_location,
        "urlList": urls_to_push
    }

    try:
        response = requests.post(endpoint, json=payload, headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print(f"Successfully pushed {len(urls_to_push)} URLs to IndexNow.")
        else:
            print(f"Failed to push to IndexNow. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    push_to_indexnow()
