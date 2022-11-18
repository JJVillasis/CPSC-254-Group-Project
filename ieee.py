# CPSC 254l Open Sources
# Steven Rico
# Group: Earth, Wind, Fire
# This file will be the main connection to the IEEE API
# It will perform a search accross the IEEE database and return a dictionary.

###IEE License###
# https://developer.ieee.org/API_Terms_of_Use2



from urllib.parse import quote_plus as url_encode
import requests
import json

class IEEE:
    def __init__(self, wildcards):
        #Primary API key: c965m6f7kxfb4f2s25jn95h4
        #Secondary API Key: j2vkkwchf2h4sde3fjtuk7k5
        self.apikey = 'c965m6f7kxfb4f2s25jn95h4'
        self._base_url = u'https://ieeexploreapi.ieee.org/api/v1/search/articles?'
        self.parameters = wildcards
        self.maxRecords = 25
        self._uri = self._base_url + '&apikey=' + self.apikey + "&max_records=" + str(self.maxRecords) + "&abstract=" + url_encode(self.parameters.lower())
        self.articles = []


    def search(self):
        resultsTable = []
        resp = requests.get(self._uri)

        if resp.status_code == 403:
            return [{"Authors": "", "Title": "", "Volume": "", "Article Number": "", "Date": "", "DOI": "", "Citations": ""}]

        results = json.loads(resp.text.encode('utf-8'))
        articles = results['articles']

        for article in articles:

            #Get all authors in article
            authors = []
            for author in article['authors']['authors']:
                authors.append(author['full_name'])

            #Get title of article
            if 'title' not in article:
                title = ""
            else: title = article['title']

            #Get the conference from which the article was written
            if 'publication_title' not in article:
                volume = ""
            else: volume = article['publication_title']

            #Get article number
            if 'publication_number' not in article:
                articleNum = ""
            else: articleNum = article['publication_number']

            #Date of the article was published
            if 'publication_year' not in article:
                date = ""
            else: date = article['publication_year']

            #Get identifier of the article
            if 'doi' not in article:
                doi = "None"
            else: doi = article['doi']

            #Get number of citations
            citations = article['citing_paper_count']

            resultsTable.append({"Authors": authors, "Title": title, "Volume": volume, "Article Number": articleNum, "Date": date, "DOI": doi, "Citations": citations})

        return resultsTable
