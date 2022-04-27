# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import json
# import argparse
# import os
# import stanza

# parser = argparse.ArgumentParser()
# parser.add_argument('keyword', help='keyword to search for')
# args = parser.parse_args()


# # Function that reads the csv specified by the args passed to the script and returns a list containing the titles of the articles and content of the articles
# def read_csv(keyword):
#     # Read the csv file
#     df = pd.read_csv("cleaned_results/"+keyword + '.csv')
#     # Get the titles and content of the articles
#     # titles = df['Title']
#     contents = df['Content']
#     # Return the titles and content
#     return contents

# # Function that runs the stanza client and returns the text
# def get_text(content):

#     # Download the stanza client
#     # stanza.download('en', 'models/')

#     # Load the stanza model and initialize it
#     nlp = stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma,depparse,ner', use_gpu=True)

#     parsed_content = nlp(content)
#     # Get the text from the parsed content
#     text = parsed_content.sentences[0].text
#     # Get the cities and countries from the parsed content
#     # cities = parsed_content.sentences[0].entities.cities

#     return cities

# # Function that loops through the list of contents and returns content 
# def get_content(contents):
#     # Loop through the list of contents
#     for content in contents:
#         text = get_text(content)
#         return text


print("NLP processing is under development and will be released soon.")