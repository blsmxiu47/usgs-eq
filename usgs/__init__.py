import requests_cache

session = requests_cache.CachedSession('http_cache', backend='filesystem')
session.params = {}

from .earthquakes import Earthquakes
