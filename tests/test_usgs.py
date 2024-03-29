import os
import sys
import logging

from dotenv import load_dotenv
from pytest import fixture
import vcr
import pandas as pd

load_dotenv()
PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
sys.path.append(PROJECT_ROOT)

from usgs import EQFeeds, EQCatalog


def get_test_download_path(download_filename, downloads_dir='test_downloads'):
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    return downloads_dir + '/' + download_filename


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
    assert set(summary_keys).issubset(response.keys()), 'All keys should be in the response'


@vcr.use_cassette('tests/vcr_cassettes/eq-get-summary-quakeml.yaml', record_mode='new_episodes')
def test_earthquakes_get_summary(summary_keys):
    """Tests USGS Earthquakes GeoJSON Feed API call to get FeatureCollection metadata"""

    eq_instance = EQFeeds()
    file_path = get_test_download_path('eq_summary_M45_day.quakeml')
    try:
        response = eq_instance.get_summary(format='quakeml', timeframe='day', min_magnitude=4.5, file_path=file_path)
    except vcr.errors.CannotOverwriteExistingCassetteException as e:
        logging.warning(e)

    assert isinstance(response, dict), "Response should be of type 'dict'"


@vcr.use_cassette('tests/vcr_cassettes/eq-query-catalog.yaml', record_mode='new_episodes')
def test_earthquakes_query_catalog():
    """Tests USGS Earthquakes GeoJSON Feed API call to get FeatureCollection metadata"""

    eq_instance = EQCatalog()
    response = eq_instance.query(response_format='geojson', start='2021-10-01', end='2021-10-03')

    assert isinstance(response, dict)
    assert response['type'] == 'FeatureCollection'


@vcr.use_cassette('tests/vcr_cassettes/eq-query-catalog-csv.yaml', record_mode='new_episodes')
def test_earthquakes_query_catalog_csv():
    """Tests USGS Earthquakes csv Feed API call to get FeatureCollection data """

    eq_instance = EQCatalog()

    downloads_dir = 'test_downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    file_path = downloads_dir + '/eq_catalog_query_october.csv'
    response = eq_instance.query(response_format='csv', file_path=file_path, start='2021-10-01', end='2021-10-03')

    assert isinstance(response, dict)
    
    df = pd.read_csv(file_path)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 777


@vcr.use_cassette('tests/vcr_cassettes/eq-query-catalog-xml.yaml', record_mode='new_episodes')
def test_earthquakes_query_catalog_xml():
    """Tests USGS Earthquakes xml Feed API call to get FeatureCollection data """

    eq_instance = EQCatalog()

    downloads_dir = 'test_downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    file_path = downloads_dir + '/eq_catalog_query_nov.xml'
    response = eq_instance.query(response_format='xml', file_path=file_path, start='2021-11-01', end='2021-11-03')

    assert isinstance(response, dict)


@vcr.use_cassette('tests/vcr_cassettes/eq-query-catalog-kml.yaml', record_mode='new_episodes')
def test_earthquakes_query_catalog_kml():
    """Tests USGS Earthquakes kml Feed API call to get FeatureCollection data """

    eq_instance = EQCatalog()

    downloads_dir = 'test_downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    file_path = downloads_dir + '/eq_catalog_query_nov.kml'
    response = eq_instance.query(response_format='kml', file_path=file_path, start='2021-11-01', end='2021-11-03')

    assert isinstance(response, dict)


@vcr.use_cassette('tests/vcr_cassettes/eq-query-catalog-text.yaml', record_mode='new_episodes')
def test_earthquakes_query_catalog_text():
    """Tests USGS Earthquakes text Feed API call to get FeatureCollection data """

    eq_instance = EQCatalog()

    downloads_dir = 'test_downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    file_path = downloads_dir + '/eq_catalog_query_nov.txt'
    response = eq_instance.query(response_format='text', file_path=file_path, start='2021-11-01', end='2021-11-03')

    assert isinstance(response, dict)
