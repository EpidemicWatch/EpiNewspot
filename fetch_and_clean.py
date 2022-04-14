import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import argparse

# Function that takes a key from RSS.json and returns the corresponding list of dictionaries.
def get_rss_data_from_json(key):
    url = get_value(key)
    return get_rss_data(url)

def get_value(key):
    with open('RSS.json') as json_file:
        data = json.load(json_file)
        return data[key]

# Function that reads RSS feeds and returns a list of dictionaries with the data from the RSS feed.
def get_rss_data(url):
    r = requests.get(url)
    # read soup in some other way than xml
    soup = BeautifulSoup(r.text, 'html.parser')
    data = []

    # Add a unique id each time a new item is added to the list and increment the id by 1
    id = 0

    for entry in soup.find_all('entry'):
        dic = {
            'id': id,
            'Title': entry.find('title', {'type': 'html'}).text,
            'Pubdate': entry.find('published').text,
            'Content': entry.find('content').text,
            'Link': entry.find('link')['href']
        }
        data.append(dic)
        id += 1
    return data

# An argparser to take in the keyword from the command line
parser = argparse.ArgumentParser()
parser.add_argument('keyword', help='keyword to search for')
args = parser.parse_args()

# Get the RSS feed url from RSS.json   
url = get_value(args.keyword)

# Loop through the url list and get the data
for url in url:
    rss_data = get_rss_data(url)

    # Create a dataframe from the list of dictionaries.
    df = pd.DataFrame(rss_data)

    df1 = pd.read_csv(f"raw_results/{args.keyword}.csv")

    df2 = pd.concat([df, df1]).drop_duplicates('Link')


    # Store the result in a csv file named the key value .csv in results folder in windows filesystem.
    df2.to_csv(f'raw_results/{args.keyword}.csv', index=False)