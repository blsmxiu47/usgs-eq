# USGS EQ Catalog API Python Wrapper
A simple Python interface for the USGS Earthquake (EQ) Catalog API, in addition to functionality for hitting the USGS Earthquakes Real-time Feed summaries.

## API Documentation
- EQ Catalog: https://earthquake.usgs.gov/fdsnws/event/1/
- Real-time Feeds (GeoJSON Summary): https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

## Usage
Instantiating Feeds:
```python
feeds = EQFeeds()

# And to get the default summary (GeoJSON)
feeds.get_summary()
```

Instantiating Catalog:
```python
catalog = EQCatalog()

# And an example query (all earthquakes within date range)
catalog.query(response_format='geojson', start='2021-10-01', end='2021-10-07')
```

## Examples
### Real-time Feeds
Past 24 hours of all earthquakes as GeoJSON:
```python
response = feeds.get_summary(format='geojson', timeframe='day')
```

Past 30 days of all earthquakes greater than or equal to M4.5 as QuakeML (XML):
```python
response = feeds.get_summary(format='quakeml', timeframe='month', min_magnitude=4.5)
```

### EQ Catalog
Rectangular location filter, 2021-10-01 through 2021-10-04 as GeoJSON, order by magnitude (desc):
```python
response = catalog.query(
    response_format='geojson', 
    start='2021-10-01', 
    end='2021-10-04',
    min_lat=32
    min_lng=-126
    max_lat=42
    max_lng=-116,
    order_by='magnitude')
```

Alternatively, download query response locally as csv and read into Pandas DataFrame:
```python
file_path = 'PATH/TO/DOWNLOAD.csv'
catalog.query(response_format='csv', file_path=file_path, start='2021-10-01', end='2021-10-04')

import pandas as pd
df = pd.read_csv(file_path)
```