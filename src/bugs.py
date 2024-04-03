import time
import re
import random
import requests

from bs4 import BeautifulSoup as Soup

max_delay = 5

def set_max_delay(delay : float):
    if delay < 1:
        delay = 1
    max_delay = delay

def find_lyrics(search_keyword : str):
    bugs_search_url = f"https://music.bugs.co.kr/search/integrated?q={search_keyword}"

    __random_delay()
    search_results = __find_music_ids_from_search_result(bugs_search_url)

    for search_result in search_results[:1]:
        music_page_url = f"https://music.bugs.co.kr/track/{search_result['music_id']}"
        __random_delay()
        lyrics = __get_lyrics_from_music_page(music_page_url)
        if lyrics is not None:
            search_result['lyrics'] = lyrics
        else:
            search_result['lyrics'] = ""
    return search_result

def __random_delay():
    time.sleep(random.random() * (max_delay - 1) + 1)

def __extract_bugsmusic_listen_parameter(input_string: str):
    # Define the regular expression pattern
    pattern = r"bugs\.music\.listen\('([^']+)',true\)"
    # Search for the pattern in the input string
    match = re.search(pattern, input_string)
    if match:
        # Extract the XXX part (group 1 in the match)
        parameter = match.group(1)
        return parameter
    else:
        return None
    
def __find_music_ids_from_search_result(url: str):
    try:
        results = []
        response = requests.get(url)
        if response.status_code == 200:
            soup = Soup(response.content, 'html.parser')
            th_elements = soup.find_all('th', scope='row')

            for th_element in th_elements:
                p_tag = th_element.find('p')
                if p_tag:
                    a_tag = p_tag.find('a')
                    if a_tag:
                        result = {"music_id":"", "title":"", "artist":""}
                        # Song title
                        title = a_tag.get('title')
                        if title:
                            result["title"] = title
                        # Artist
                        td_tag = th_element.find_next_sibling('td')
                        p_artist = td_tag.find('p', class_='artist')
                        if p_artist:
                            a_tag2 = p_artist.find('a')
                            if a_tag2:
                                result["artist"] = a_tag2.get_text()
                        # Lyrics
                        onclick_event = a_tag.get('onclick')
                        if onclick_event:
                            result['music_id'] = __extract_bugsmusic_listen_parameter(onclick_event)

                        results.append(result)
            return results
        else:
            print("Error: Unable to fetch the content from the URL")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def __get_lyrics_from_music_page(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = Soup(response.content, 'html.parser')
            lyrics_container_div = soup.find('div', class_='lyricsContainer')
            if lyrics_container_div:
                xmp_tag = lyrics_container_div.find('xmp')
                if xmp_tag:
                    return xmp_tag.get_text()
                else:
                    print("No <xmp> tag found inside the <div> with class 'lyricsContainer'")
            else:
                print("No <div> tag with class 'lyricsContainer' found")
        else:
            print("Error: Unable to fetch the content from the URL")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
