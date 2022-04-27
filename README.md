# NewsSpot

NewsSpot is a tool that scrapes real-time data from RSS feeds to recognize patterns in Outbreak Detection.

## About the Project

NewsSpot scrapes off data from RSS feeds from Google Alerts pertaining to user-defined Diseases and performs NLP using [Stanza](https://github.com/stanfordnlp/stanza). The resultant data is then constructed towards predicting Outbreaks of mentioned diseases or their variants thorugh symptom analysis.

## Built With

Python packages required to run:
- BeautifulSoup
- Requests
- Pandas
- Regex
- OS
- Stanza

## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

#### Prerequisites
The following command will install the packages according to the configuration file requirements.txt.
```
$ pip install -r requirements.txt
```

Stanza is a Python package that is used to perform NLP on the scraped data. To install Stanza, follow the instructions on the [Stanza](https://github.com/stanfordnlp/stanza) and download the model.

Alternatively, you can uncomment `line 28` in `NLP.py` to install Stanza.
```
# Download the stanza client
# stanza.download('en', 'models/')
```

## Usage

##### Adding New Disease Alerts
- Setup your Google Alerts in the `RSS.json` file.
- Add your specific disease RSS feed link under their respective key-value pair.
- New RSS feed additions to pre-existing diseases shall be added at the end of the disease list in the `RSS.json`

##### Running the Project

- Run the `fetch_and_clean.py` to scrape all the RSS feeds and store it in `raw_results`. New feed will be overwritten at the end of the CSVs
- The `fetch_and_clean.py` needs an disease argument to load into memory. For example, `python3 fetch_and_clean.py covid`
- Run the `data_preprocess.py` to clean the CSVs in `raw_results` and prepare for NLP
- Run the `content_processor.py` to get the entire text data from each article in the feed.
- Run the `NLP.py`

Alternatively, you can run the `main.py` directly with the arguments of all the disease you want to process.
```
$ python3 main.py covid corona measles
```

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License
