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

usage: `fetch.py [-h] [--out OUT] [--verbose] query`

positional arguments:  
- `query`: Search query string, or Input file path of search queries. Whether it is a file or not is determined by the dot(.).  

optional arguments:  
- `-h`, `--help`: Show help message  
- `--out OUT`: Output file path. Outputs to standard output if not specified.  
- `--verbose`: Prints current queries and progress. Defaults to `False`
```
// Single query, output to file, log process
python fetch.py BETELGEUSE --out result.txt --verbose

// Multiple queries, output to standard output
python fetch.py queries.txt
```

## About
Calling `bugs.find_lyrics(song_name)` will return a json object (or a dictionary) containing the first song's title, artist, and lyrics, searched from bugs.
If some information such as lyrics are not found, it will be empty.