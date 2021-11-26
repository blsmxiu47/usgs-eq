from . import session
from .urls import Urls

# import logging

class Earthquakes(object):
    def __init__(self) -> None:
        super().__init__()

        self.url = Urls()

    def get_summary(self, format='geojson', timeframe='hour', min_magnitude=None):
        """
        GETs pre-defined summary reports from USGS Earthquake Hazards Program Real-time Feeds. 
        These reports are suitable for regularly updating with recent data (up to past 30 days, updated every minute).

        format (str) -- the file format in which to request the response ('geojson', 'atom', 'kml', 'csv', 'quakeml')
        timeframe (str) -- 'hour', 'day', 'week', or 'month' for past hour, 24 hours, 7 days, 30 days respectively
        min_magnitude (str, int, or float) -- optional, minimum magnitude for the summary (available for '1.0', '2.5', '4.5', and 'significant')
        """
        if min_magnitude is None:
            min_magnitude = 'all'
        else:
            min_magnitude = str(float(min_magnitude))
            assert min_magnitude in ['1.0', '2.5', '4.5', 'significant'], \
                "argument min_magnitude takes values '1.0', '2.5', '4.5', and 'significant'. For more specific filtering please use the EQ Catalog method, query_catalog"
        
        path = f'{self.url.summary_url()}{min_magnitude}_{timeframe}.{format}'
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
