import requests
import json

apiAddr = "https://itunes.apple.com/search"

def GetSongTitle(keyword):
    
    # 1. Create a dictionary will store parameters

    ds = {}
    
    # 2. Add key and value to set parameters

    ds["term"] = keyword
    ds["country"] = "US"
    ds["media"] = "music"
    ds["limit"] = "20"

    # 3. Make requests

    response = requests.get(apiAddr, params=ds)

    # 4. Store json data received from Api

    jsonRes = json.loads(response.text)

    # 5. Iterate through dictionary and filter them by user input

    for i in jsonRes["results"]:
        decodedText = ((i)["trackName"]) 
	print(decodedText)


term = raw_input("Put any words related to music : ")

GetSongTitle(term)
