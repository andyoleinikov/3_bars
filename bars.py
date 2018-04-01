import json
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return False


def get_biggest_bar(data):
    bars_list = []
    for feature in data['features']:
        bar_name = feature['properties']['Attributes']['Name']
        seats_count = feature['properties']['Attributes']['SeatsCount']
        bars_list.append((bar_name, seats_count))
    biggest_bar = max(bars_list, key=lambda item: item[1])
    return biggest_bar[0]


def get_smallest_bar(data):
    bars_list = []
    for feature in data['features']:
        bar_name = feature['properties']['Attributes']['Name']
        seats_count = feature['properties']['Attributes']['SeatsCount']
        bars_list.append((bar_name, seats_count))
    smallest_bar = min(bars_list, key=lambda item: item[1])
    return smallest_bar[0]


def get_closest_bar(data, longitude, latitude):
    bars_list = []
    for feature in data['features']:
        bar_name = feature['properties']['Attributes']['Name']
        bar_longitude, bar_latitude = feature['geometry']['coordinates']
        distance = ((longitude - float(bar_longitude))**2 +
                    (latitude - float(bar_latitude))**2)**(1 / 2)
        bars_list.append((bar_name, distance))
    closest_bar = min(bars_list, key=lambda item: item[1])
    return closest_bar[0]


if __name__ == '__main__':
    filepath = input('Input file path or "bars.json" is used: ')
    data = load_data(filepath) or load_data('bars.json')
    if data:
        print('Biggest bar is:', get_biggest_bar(data))
        print('Smallest bar is:', get_smallest_bar(data))

        try:
            longitude = float(input('Input your longitude: '))
        except ValueError:
            print('Incorrect input, using 0 as longitude')
            longitude = 0

        try:
            latitude = float(input('Input your latitude: '))
        except ValueError:
            print('Incorrect input, using 0 as latitude')
            latitude = 0

        print('Closest bar is:', get_closest_bar(data, longitude, latitude))
    else:
        print('Wrong file or path')
