from usgs import EQFeeds, EQCatalog
import pandas as pd
import os

if __name__ == '__main__':
    feeds = EQFeeds()

    # Get summary of all earthquakes in the past hour as GeoJSON
    earthquakes_all_pasthour = feeds.get_summary()
    print(type(earthquakes_all_pasthour), '\nKeys:\n', earthquakes_all_pasthour.keys())

    catalog = EQCatalog()

    # Query EQ Catalog for 2021 Oct 1st ~ 2021 Oct 4th
    earthquakes_geojson_oct = catalog.query(response_format='geojson', start='2021-10-01', end='2021-10-04')
    print(type(earthquakes_geojson_oct), '\nKeys:\n', earthquakes_geojson_oct.keys())

    # Alternatively save csv version of query response and read into Pandas df
    file_path = 'earthquakes_oct_sample.csv'
    earthquakes_csv_response = catalog.query(response_format='csv', file_path=file_path, start='2021-10-01', end='2021-10-04')
    df = pd.read_csv(file_path)
    print(df.head())
    os.remove(file_path)
