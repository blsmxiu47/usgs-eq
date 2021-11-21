import sys
# print(sys.path)
sys.path.append('C:\\Users\\weswa\\Projects\\py-natural-events\\earthquakes\\usgs')
from usgs import Earthquakes

def test_earthquakes_get_summary():
    """Tests USGS Earthquakes GeoJSON Feed API call to get FeatureCollection metadata"""

    eq_instance = Earthquakes()
    response = eq_instance.get_summary(start="2021-10-01", end="2021-10-31")

    assert isinstance(response, dict)
    assert response['type'] == 'FeatureCollection'
