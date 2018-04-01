import json
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return False


def get_biggest_bar(bars_json):
    bars_list = []
    for feature in bars_json['features']:
        bar_name = feature['properties']['Attributes']['Name']
        seats_count = feature['properties']['Attributes']['SeatsCount']
        bars_list.append((bar_name, seats_count))
    biggest_bar = max(bars_list, key=lambda item: item[1])
    return biggest_bar[0]


def get_smallest_bar(bars_json):
    bars_list = []
    for feature in bars_json['features']:
        bar_name = feature['properties']['Attributes']['Name']
        seats_count = feature['properties']['Attributes']['SeatsCount']
        bars_list.append((bar_name, seats_count))
    smallest_bar = min(bars_list, key=lambda item: item[1])
    return smallest_bar[0]


def get_closest_bar(bars_json, longitude, latitude):
    bars_list = []
    for feature in bars_json['features']:
        bar_name = feature['properties']['Attributes']['Name']
        bar_longitude, bar_latitude = feature['geometry']['coordinates']
        distance = ((longitude - float(bar_longitude))**2 +
                    (latitude - float(bar_latitude))**2)**(1 / 2)
        bars_list.append((bar_name, distance))
    closest_bar = min(bars_list, key=lambda item: item[1])
    return closest_bar[0]


def coordinate_to_float(coordinate_str):
    try:
        coordinate = float(coordinate_str)
        return coordinate
    except ValueError as e:
        return False


def process_bars(bars_json):
    print('Biggest bar is:', get_biggest_bar(bars_json))
    print('Smallest bar is:', get_smallest_bar(bars_json))

    longitude = coordinate_to_float(input('Input your longitude: '))
    latitude = coordinate_to_float(input('Input your latitude: '))

    if longitude and latitude:
        print('Closest bar is:',
              get_closest_bar(bars_json, longitude, latitude))
    else:
        print('Wrong coordinates')


if __name__ == '__main__':
    filepath = input('Input file path or "bars.json" is used: ')
    bars_json = load_data(filepath) or load_data('bars.json')
    if bars_json:
        process_bars(bars_json)
    else:
        print('Wrong file or path')
