from usgs import EQFeeds, EQCatalog

if __name__ == '__main__':
    feeds = EQFeeds()

    earthquakes_all_pasthour = feeds.get_summary()
    print(type(earthquakes_all_pasthour), '\nKeys:\n', earthquakes_all_pasthour.keys())

    catalog = EQCatalog()

    earthquakes_geojson_oct = catalog.query(response_format='geojson', start='2021-10-01', end='2021-10-04')
    print(type(earthquakes_geojson_oct), '\nKeys:\n', earthquakes_geojson_oct.keys())
