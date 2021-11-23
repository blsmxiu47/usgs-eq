from . import session

class Earthquakes(object):
    def __init__(self) -> None:
        super().__init__()    


    def get_summary(self, timeframe='hour', min_magnitude=None):
        if min_magnitude is None:
            min_magnitude = 'all'
        else:
            min_magnitude = str(min_magnitude)
            assert min_magnitude in ['1.0', '2.5', '4.5', 'significant']
        path = f'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{min_magnitude}_{timeframe}.geojson'
        response = session.get(path)
        return response.json()


    def get_geojson(self, start='2021-01-01', end='2021-01-02'):
        path = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start}&endtime={end}'
        response = session.get(path)
        return response.json()
