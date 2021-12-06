import time

from . import session


def make_request(url, format='geojson', params=None, file_path=None):
    if format != 'geojson':
        with session.get(url, params=params) as response:
            response.raise_for_status()
            if file_path is None:
                file_path = 'usgs_response_{0}.{1}'.format(time.time(), params['format'])
            with open(file_path, 'wb+') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return {'response': response, 'user_parameters': params}
    else:
        response = session.get(url, params=params)
        return response.json()
