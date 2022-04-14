import pandas as pd
import os
import re
import json
import argparse
import stanza
import requests
from bs4 import BeautifulSoup

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}


def get_text_from_link(url):
    resp = requests.get(url, headers=agent)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    
    html_page = resp.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'style',
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
            
    newOutput = output.replace("\n", '')
    newOutput = newOutput.replace("\t", '')

    return newOutput

# Loop through all csv files in the cleaned_results folder
files = os.listdir('cleaned_results')

for file in files:
    # Read the files in cleaned_results folder
    df = pd.read_csv(f"cleaned_results/{file}")

    # Loop through column Link
    for index, row in df.iterrows():
        # Get the link
        link = row['Link']
        # Get the text from the link
        text = get_text_from_link(link)
        # Add the text to the dataframe
        df.at[index, 'Content'] = text

    # Overwrite the file in cleaned_results folder
    df.to_csv(f"cleaned_results/{file}", index=False)
    