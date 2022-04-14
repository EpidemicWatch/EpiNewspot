import pandas as pd
import os
import re
import json
import argparse

# Loop through all csv files in the raw_results folder
files = os.listdir('raw_results')

def clean_link(link):
    start = link.find('url=')
    end = link.find('&ct=')
    link = link[start+4:end]
    return link

# Loop through all files in the raw_results folder
for file in files: 

    # check if file is present in cleaned_results folder
    if os.path.isfile(f"cleaned_results/{file}"):
        df1 = pd.read_csv(f"cleaned_results/{file}")
    else:
        # store the file in cleaned_results folder
        df1 = pd.read_csv(f"raw_results/{file}",)
        df1.to_csv(f"cleaned_results/{file}", index=False)


cleanFiles = os.listdir('cleaned_results')

for file in cleanFiles:
    # Read the files in cleaned_results folder
    df2 = pd.read_csv(f"cleaned_results/{file}")
    # delete pubdate column and content column if present
    if 'Pubdate' in df2.columns:
        df2 = df2.drop(columns=['Pubdate'])
    if 'Content' in df2.columns:
        df2 = df2.drop(columns=['Content'])


    # Loop through column Link and clean the links
    for index, row in df2.iterrows():
        df2.at[index, 'Link'] = clean_link(row['Link'])

    # Overwrite the file in cleaned_results folder
    df2.to_csv(f"cleaned_results/{file}", index=False)
    
    

