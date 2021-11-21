class Earthquakes(object):
    def __init__(self) -> None:
        super().__init__()
    
    def get_summary(self, start="2021-01-01", end="2021-01-02"):
        return {'type': 'FeatureCollection'}
