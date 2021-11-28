# Modified Code from https://github.com/juliomalegria/python-craigslist, MIT-zero license

import logging

class EQCatalogBase(object):
    """" Base class for EQ Catalog wrappers """

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

    def __init__(self, params=None):
        self.params = self.get_params(params)

    def get_params(self, params):
        """ Parses parameters passed by the user into GET parameters """

        parsed_params = {}

        for key, val in params.items():
            try:
                param = self.default_params.get(key)
                if param['value'] is None:
                    parsed_params[param['url_key']] = param['value']
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
            except KeyError:
                logging.warning(f'{key} is not a valid option')
        return parsed_params
