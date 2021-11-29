import sys
# print(sys.path)
sys.path.append('C:\\Users\\weswa\\Projects\\py-natural-events\\earthquakes\\usgs')
import logging

from pytest import fixture
import vcr

from usgs import EQFeeds, EQCatalog


@fixture
def summary_keys():
    return ['type', 'metadata', 'features', 'bbox']


@vcr.use_cassette('tests/vcr_cassettes/eq-get-summary.yaml', record_mode='new_episodes')
def test_earthquakes_get_summary(summary_keys):
    """Tests USGS Earthquakes GeoJSON Feed API call to get FeatureCollection metadata"""

    eq_instance = EQFeeds()
    try:
        response = eq_instance.get_summary()
    except vcr.errors.CannotOverwriteExistingCassetteException as e:
        logging.warning(e)

    assert isinstance(response, dict), "Response should be of type 'dict'"
    assert response['type'] == 'FeatureCollection', "Response 'type' should be 'FeatureCollection'"
    assert set(summary_keys).issubset(response.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/vcr_cassettes/eq-query-catalog.yaml', record_mode='new_episodes')
def test_earthquakes_query_catalog():
    """Tests USGS Earthquakes GeoJSON Feed API call to get FeatureCollection metadata"""

    eq_instance = EQCatalog()
    response = eq_instance.query(response_format='geojson', start='2021-10-01', end='2021-10-03')

    assert isinstance(response, dict)
    assert response['type'] == 'FeatureCollection'
