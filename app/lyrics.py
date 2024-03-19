import requests

GENIUS_API_KEY = "UFQ50wN0KNMrl2-xZxHRUnjG1CgbOgyaCzCECGwf6GpnN8bgnDFMKH6WRsY9ZrXU"  # Replace with your actual Genius API key

def get_lyrics(artist_name, song_title):
    headers = {"Authorization": "Bearer " + GENIUS_API_KEY}
    search_url = f"https://api.genius.com/search?q={artist_name} {song_title}"
    
    response = requests.get(search_url, headers=headers)
    response_json = response.json()
    
    if "error" in response_json:
        print("Error:", response_json["error"])
        return None
    
    hits = response_json["response"]["hits"]
    
    for hit in hits:
        if artist_name.lower() in hit["result"]["primary_artist"]["name"].lower():
            lyrics_url = hit["result"]["url"]
            return fetch_lyrics(lyrics_url)
    
    print("Lyrics not found.")
    return None

def fetch_lyrics(lyrics_url):
    response = requests.get(lyrics_url)
    
    if response.status_code == 200:
        lyrics_html = response.text
        start_tag = '<div class="lyrics">'
        end_tag = '<!--/sse-->'
        
        start_index = lyrics_html.find(start_tag)
        end_index = lyrics_html.find(end_tag, start_index)
        
        if start_index != -1 and end_index != -1:
            lyrics_text = lyrics_html[start_index + len(start_tag):end_index].strip()
            return lyrics_text
    
    print("Failed to fetch lyrics.")
    return None