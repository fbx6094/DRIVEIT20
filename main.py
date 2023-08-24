import json
import pandas as pd

with open('docks.json', 'r') as file:
    docks_data = json.load(file)

# Загрузка JSON файла с данными об автобусах
with open('ships.json', 'r') as file:
    ships_data = json.load(file)

# Загрузка JSON файла с данными о расписании
with open('schedule.json', 'r') as file:
    schedule_data = json.load(file)

# # Загрузка JSON файла с данными о маршрутах
# with open('routes.json', 'r') as file:
#     routes_data = json.load(file)

docks_df = pd.DataFrame(docks_data)
docks_df.to_csv('docks.csv', index=False)

ships_df = pd.DataFrame(ships_data)
ships_df.to_csv('ships.csv', index=False)

schedule_df = pd.DataFrame(schedule_data)
schedule_df.to_csv('schedule.csv', index=False)

trips_data = {
    'route_id':[],
    'service_id':[],
    'trip_id':[],
    'trip_headsign':[],
    'block_id':[]
}

trips_df = pd.DataFrame(trips_data)
trips_df.to_csv('trips.csv', index=False)

stop_times_data = {
    'trip_id':[],
    'arrival_time':[],
    'departure_time':[],
    'stop_id':[],
    'stop_sequence':[],
    'pickup_type':[],
    'drop_off_type':[]
}

stop_times_df = pd.DataFrame(stop_times_data)
stop_times_df.to_csv('stop_times.csv', index=False)