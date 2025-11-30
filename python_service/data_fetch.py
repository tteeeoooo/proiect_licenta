import fastf1
fastf1.Cache.enable_cache('f1_cache')

session = fastf1.get_session(2024, 'Monza', 'Race')
session.load()

print(session.laps.columns)
print(session.drivers)
print(session.results)
print(session.weather_data)