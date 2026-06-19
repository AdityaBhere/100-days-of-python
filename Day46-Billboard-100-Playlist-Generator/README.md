# Billboard Playlist Creator

## Overview

This project automatically creates a private YouTube Music playlist containing the Billboard Top 100 songs from any selected date.

The user enters a date in the format:

YYYY-MM-DD

The program then:

1. Scrapes song titles from a Billboard-style chart page.
2. Searches each song on YouTube Music.
3. Creates a playlist if it does not already exist.
4. Adds all discovered songs to the playlist automatically.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* YouTube Music API (ytmusicapi)

## Important Note

This project does **not** use the official Billboard Hot 100 website.

The official Billboard website requires paid access and additional scraping restrictions.

As part of the course resources, a Billboard-style dataset hosted by App Brewery is used instead:

https://appbrewery.github.io/bakeboard-hot-100/

## Setup

### 1. Clone the repository

```bash
git clone github.com/AdityaBhere/100-days-of-python/tree/master/Day46-Billboard-100-Playlist-Generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create browser.json

Before running the project you must authenticate with YouTube Music and generate a browser.json file.

Follow the ytmusicapi authentication guide and place the generated browser.json file in the project directory.

### 4. Update User-Agent

Replace the User-Agent in the code with your own browser's User-Agent string.

Example:

```python
headers = {
    "User-Agent": "YOUR USER AGENT HERE"
}
```

### 5. Run the project

```bash
python main.py
```

Enter a date:

```text
2026-01-01
```

The program will create a private YouTube Music playlist and populate it with the songs from that date.

## Features

* Scrapes Top 100 song titles
* Creates playlists automatically
* Prevents duplicate playlists
* Searches songs using YouTube Music
* Handles missing songs gracefully
* Automates playlist population

## Learning Outcomes

Through this project I learned:

* Web scraping using BeautifulSoup
* Parsing HTML data
* Working with APIs
* Playlist automation
* Error handling in Python
* Managing authentication files securely

```
```
