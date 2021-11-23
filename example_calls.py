from usgs import Earthquakes

eq = Earthquakes()
earthquakes_all_pasthour = eq.get_summary()

print(type(earthquakes_all_pasthour))
print('Keys:')
print(earthquakes_all_pasthour.keys())