import logging

from . import session
from .urls import Urls
# from .base import EQCatalogBase

# class EQCatalog(EQCatalogBase):
#     def __init__(self) -> None:
#         logging.info('EQCatalog using Base...')


class EQCatalog(object):

    default_params = {
        'response_format': {'url_key': 'format', 'value': None},
        'start': {'url_key': 'starttime', 'value': None},
        'end': {'url_key': 'endtime', 'value': None},
        'updated_after': {'updatedafter': 'format', 'value': None},
        'min_lat': {'url_key': 'minlatitude', 'value': None},
        'min_lng': {'url_key': 'minlongitude', 'value': None},
        'max_lat': {'url_key': 'maxlatitude', 'value': None},
        'max_lng': {'url_key': 'maxlongitude', 'value': None},
        'max_radius': {'url_key': 'maxradius', 'value': None},
        'max_radius_km': {'url_key': 'maxradiuskm', 'value': None},
        'catalog': {'url_key': 'catalog', 'value': None},
        'contributor': {'url_key': 'contributor', 'value': None},
        'eventid': {'url_key': 'eventid', 'value': None},
        'include_all_magnitudes': {'url_key': 'includeallmagnitudes', 'value': None},
        'include_all_origins': {'url_key': 'includeallorigins', 'value': None},
        'include_arrivals': {'url_key': 'includearrivals', 'value': None},
        'include_deleted': {'url_key': 'includedeleted', 'value': None},
        'include_superseded': {'url_key': 'includesuperseded', 'value': None},
        'limit': {'url_key': 'limit', 'value': None},
        'min_depth': {'url_key': 'mindepth', 'value': None},
        'min_magnitude': {'url_key': 'minmagnitude', 'value': None},
        'max_depth': {'url_key': 'maxdepth', 'value': None},
        'max_magnitude': {'url_key': 'maxmagnitude', 'value': None},
        'offset': {'url_key': 'offset', 'value': 1},
        'order_by': {'url_key': 'orderby', 'value': 'time'},
    }

    def __init__(self, params=default_params):
        self.url = Urls().query_url()

    def get_params(self, params):
        """ Parses parameters passed by the user into GET parameters """

        parsed_params = {}

        for key, val in params.items():
            print(key, val)
            try:
                param = self.default_params.get(key)
                print(param)
                if param['value'] is None:
                    parsed_params[param['url_key']] = val
                elif isinstance(param['value'], dict):
                    valid_options = param['value']
                    if isinstance(val, str):
                        val = [val]
                    options = []
                    for opt in val:
                        try:
                            options.append(valid_options[opt])
                        except KeyError:
                            logging.warning(f'{(opt, key)} is not a valid option')
                    parsed_params[param['url_key']] = options
                elif val:
                    parsed_params[param['url_key']] = param['value']
                print(param['value'])
            except KeyError:
                logging.warning(f'{key} is not a valid option')
        print(parsed_params)
        return parsed_params

    def query(self, **kwargs):
        """ Executes GET request of USGS EQ Catalog API using filters specified by user in method parameters """
        params = self.get_params(kwargs)
        response = session.get(self.url, params=params)
        return response.json()


class EQFeeds(object):
    def __init__(self) -> None:
        super().__init__()

        self.url = Urls().summary_url()

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
        
        path = f'{self.url}{min_magnitude}_{timeframe}.{format}'
        response = session.get(path)
        return response.json()
