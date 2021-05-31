from youtubesearchpython import SearchVideos
import json


def youtube_searcher(song_name):
    search = SearchVideos(song_name, offset=1, mode="json", max_results=5)
    a = json.loads(search.result())

    return a['search_result'][0]['title'], a['search_result'][0]['link']
