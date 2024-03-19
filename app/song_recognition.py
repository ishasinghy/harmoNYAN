import pyacoustid

def recognize_song(audio_file):
    apikey = "WcczHagjdG"  # Replace with your actual Acoustid API key

    try:
        duration, fingerprint = pyacoustid.fingerprint_file(audio_file)
        matches = pyacoustid.lookup(apikey, fingerprint, duration)
        
        result = []
        for score, recording_id, title, artist in pyacoustid.parse_lookup_result(matches):
            result.append({
                "score": score,
                "recording_id": recording_id,
                "title": title,
                "artist": artist
            })
        
        return result

    except pyacoustid.FingerprintGenerationError as e:
        print("Fingerprint generation error:", e)
    except pyacoustid.WebServiceError as e:
        print("Web service error:", e)
    
    return None