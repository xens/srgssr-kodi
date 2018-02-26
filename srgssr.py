#!/usr/bin/python3

import requests
import json

def get_tv_shows():
    """
    Get a list of all the TV show provided by the BU (SFR, SSR, SRI, ...)
    """
    listOfTvShows = []
    req = requests.get(url="http://srgssr-prod.apigee.net/integrationlayer/2.0/rts/showList/tv/alphabetical?apikey=nhm23AYwrCfzsK5aVuCB39gfzeGc3T5k&pageSize=unlimited") 
    output = json.loads(req.content) 

    for i in output['showList']:
        listOfTvShows.append(i['title'])

    print(listOfTvShows)
    return listOfTvShows
