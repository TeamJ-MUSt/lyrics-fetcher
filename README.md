# lyrics-fetcher
Python script that will search for japanese song's lyrics.

## Environment
Python 3.9.12

## How to run
1. Clone this repository
```
git clone https://github.com/TeamJ-MUSt/lyrics-fetcher
cd lyrics-fetcher
```
2. Install `requirements.txt`
```
pip install -r requirements.txt
```
3. Run `fetch.py` with arguments
```
// Single query
python fetch.py --query BETELGEUSE --out result.txt

// Multiple queries from file
python fetch.py --query queries.txt --out results.txt
```

## About
Calling `bugs.find_lyrics(song_name)` will return a json object (or a dictionary) containing the first song's title, artist, and lyrics, searched from bugs.
If some information such as lyrics are not found, it will be empty.