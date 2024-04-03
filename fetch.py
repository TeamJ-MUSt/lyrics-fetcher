import argparse
import json
import os

from src import bugs

bugs.max_delay = 3

def is_file(string):
    _, file_extension = os.path.splitext(string)
    return bool(file_extension)

def get_query_result(search_query):
    query = search_query.strip()
    print("Querying:", query)
    return bugs.find_lyrics(query)

def main():
    parser = argparse.ArgumentParser(description='Fetch lyrics from bugs')
    parser.add_argument('--query', help='Search query string, or Input file path of search queries')
    parser.add_argument('--out', help='Output file path', required = True)
    args = parser.parse_args()

    if not args.out:
        print("Error: Please provide an output file path using --out")
        return
    if not args.query:
        print("Error: Please provide an query using --query")
        return
    results = []
    if is_file(args.query):
        with open(args.query, 'r', encoding='UTF-8') as file:
            for line in file:
                query_result = get_query_result(line.strip())
                results.append(query_result)
    else:
        query_result = get_query_result(args.query)
        results.append(query_result)

    with open(args.out, 'w', encoding='UTF-8') as json_file:
        json.dump(results, json_file, indent=4, ensure_ascii=False)
        print("Saved results as json:", args.out)

if __name__ == "__main__":
    main()