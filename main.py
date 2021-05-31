import songlist_getter
import youtube_search
import downloader
import time
import csv
if __name__ == "__main__":
    playlist_id = input("Enter playlist id:")
    log = open('songs.csv','w', newline='')
    fieldnames = ['name','status', 'youtube name']
    writer = csv.DictWriter(log, fieldnames=fieldnames)
    writer.writeheader()
    tracks = songlist_getter.getTrackNames(playlist_id)

    for track in tracks:
        search_res = youtube_search.youtube_searcher(track)
        download_result = downloader.download(search_res[1], track)
        print({
        'status': download_result[1], 
        'name': track,
        'youtube name': search_res[0],
        'stream': download_result[0]})
        try:
            writer.writerow({
            'status': download_result[1],
            'name': track,
            'youtube name': search_res[0]})
        except:
            pass
        time.sleep(1)
