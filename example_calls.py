from usgs import Earthquakes

if __name__ == '__main__':
    eq = Earthquakes()

    earthquakes_all_pasthour = eq.get_summary()
    print(type(earthquakes_all_pasthour), '\nKeys:\n', earthquakes_all_pasthour.keys())

    earthquakes_geojson_oct = eq.query_catalog(response_format='geojson', start='2021-10-01', end='2021-10-04')
    print(type(earthquakes_geojson_oct), '\nKeys:\n', earthquakes_geojson_oct.keys())
