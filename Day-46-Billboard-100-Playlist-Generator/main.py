import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
headers = {
    "User-Agent": #add your own user agent
}

response = requests.get(url=f"https://appbrewery.github.io/bakeboard-hot-100/{date}", headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="h3", class_="chart-entry__title")
song_names = [song.getText().strip() for song in songs]

yt = YTMusic("browser.json")

playlists = yt.get_library_playlists()

no_playlist_with_same_name = True
playlist_id = None

for playlist_title in playlists:
    if playlist_title["title"] == f"{date} Billboard 100":
        print("Playlist with the same name already exists....")
        no_playlist_with_same_name = False
        playlist_id = playlist_title["playlistId"]

if no_playlist_with_same_name:
    playlist_id = yt.create_playlist(
        title=f"{date} Billboard 100",
        description="Part of a project",
        privacy_status="PRIVATE"
    )
    print("Playlist created successfully....")

for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=5)
        if search_results:
            yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
            print(f"Added: {song}")
        else:
            print(f"Skipped: {song} | Reason: Song not found on YouTube Music")

    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
