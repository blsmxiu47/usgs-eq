from . import session
from .urls import Urls

class Earthquakes(object):
    def __init__(self) -> None:
        super().__init__()

        self.url = Urls()

    def get_summary(self, timeframe='hour', min_magnitude=None):
        """

        timeframe String: 
        """
        if min_magnitude is None:
            min_magnitude = 'all'
        else:
            min_magnitude = str(min_magnitude)
            assert min_magnitude in ['1.0', '2.5', '4.5', 'significant']
        path = f'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{min_magnitude}_{timeframe}.geojson'
        response = session.get(path)
        return response.json()

    def query_catalog(self, response_format='geojson', start='2021-01-01', end='2021-01-02'):
        """
        Parameters:
            response_format (str) -- file format in which to return summary and catalog responses (e.g. 'atom', 'csv', 'geojson', 'kml', 'xml')
            start (str) -- Start date of time period to search (format: %Y-%m-%d)
            end (str) -- End date of time period to search (format: %Y-%m-%d)
        """
        path = f'{self.url.query_url()}format={response_format}&starttime={start}&endtime={end}'
        response = session.get(path)
        return response.json()
