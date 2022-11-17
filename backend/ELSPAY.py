from urllib.parse import quote_plus as url_encode
import pandas as pd
import requests
import json

class Elsa:
    def __init__(self, query):
        # Initializes a search object with a query and target index.
        self.query = query
        self.index = 'scopus'
        self.apikey = 'e989909fd8d4e4aa2f99a9a73606b55f'
        self._base_url = u'https://api.elsevier.com/content/search/'
        self._uri = self._base_url + self.index + '?query=' + url_encode(
                self.query)
        self.counter = 0
        self.id_list = []
        self.results = []
        

    def search(self):
        resp = requests.get(self._uri,
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': self.apikey})

        results = resp.json()

        for r in results['search-results']["entry"]:
            if self.counter < 2:
                id = str(r['dc:identifier'])
                self.id_list.append(id)
                self.counter += 1
            else:
                self.counter = 0
                break

        for id in self.id_list:
            result = self.get_scopus_info(id)
            self.results.append(result)

        return self.results

    def get_scopus_info(self, SCOPUS_ID):
        url = ("http://api.elsevier.com/content/abstract/scopus_id/"
            + SCOPUS_ID
            + "?field=authors,title,publicationName,volume,issueIdentifier,"
            + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
        resp = requests.get(url,
                        headers={'Accept':'application/json',
                                'X-ELS-APIKey': 'e989909fd8d4e4aa2f99a9a73606b55f'})
        results = json.loads(resp.text.encode('utf-8'))
        authors = []
        
        
        for au in results['abstracts-retrieval-response']['authors']['author']:
            auth=''.join(au['ce:indexed-name'])
            authors.append(auth)

        title=results['abstracts-retrieval-response']['coredata']['dc:title'].encode('utf-8')

        journal=results['abstracts-retrieval-response']['coredata']['prism:publicationName'].encode('utf-8')

        volume=results['abstracts-retrieval-response']['coredata']['prism:volume'].encode('utf-8')
        
        articlenum=(results['abstracts-retrieval-response']['coredata'].get('prism:pageRange') or
                    results['abstracts-retrieval-response']['coredata'].get('article-number')).encode('utf-8')
        
        date=results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8')
        
        doi='doi:' + str(results['abstracts-retrieval-response']['coredata']['prism:doi'].encode('utf-8'))
        
        cites=int(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8'))

        DICT = {'authors' : authors, 'title': title.decode('utf-8'), 'journal': journal.decode('utf-8'), 'volume': volume.decode('utf-8'), 'articlenum': articlenum.decode('utf-8'), 'date': date.decode('utf-8'), 'doi': doi, 'cites': cites}
        return DICT