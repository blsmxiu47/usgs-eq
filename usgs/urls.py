class Urls:
    def __init__(self):
        """ Defines base and endpoint urls in one place to make updating the package simpler if/when the official API is updated """
        self.base_url = 'https://earthquake.usgs.gov/'
        
        self.summary_base_url = self.base_url + 'earthquakes/feed/v1.0/summary/'
        
        self.events_base_url = self.base_url + 'fdsnws/event/1/'
        self.application_json = 'application.json'
        self.application_wadl = 'application.wadl'
        self.catalogs = 'catalogs'
        self.contributors = 'contributors'
        self.query = 'query?'
        self.version = 'version'
    
    def base_url(self):
        return self.base_url

    def application_json_url(self):
        return self.events_base_url + self.application_json

    def application_wadl_url(self):
        return self.events_base_url + self.application_wadl

    def catalogs_url(self):
        return self.events_base_url + self.catalogs

    def contributors_url(self):
        return self.events_base_url + self.contributors

    def version_url(self):
        return self.events_base_url + self.version

    def summary_url(self):
        return self.summary_base_url

    def query_url(self):
        return self.events_base_url + self.query
