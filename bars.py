import json
import os
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as bars_file:
            return json.load(bars_file)
    return None


def get_biggest_bar(bars_list):
    biggest_bar = max(
        bars_list,
        key=lambda item: item['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bars_list):
    smallest_bar = min(
        bars_list,
        key=lambda item: item['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def get_closest_bar(bars_list, longitude, latitude):
    closest_bar = min(
        bars_list,
        key=lambda item:
        (
            (longitude - item['geometry']['coordinates'][0])**2 +
            (latitude - item['geometry']['coordinates'][1])**2
        )**(1 / 2)
    )
    return closest_bar


def coordinate_to_float(coordinate_str):
    try:
        coordinate = float(coordinate_str)
        return coordinate
    except ValueError:
        return None


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')

    filepath = sys.argv[1]
    bars_dict = load_data(filepath)
    if bars_dict is None:
        sys.exit('Wrong file')

    bars_list = bars_dict['features']

    print(
        'Biggest bar name is:',
        get_bar_name(get_biggest_bar(bars_list))
    )

    print(
        'Smallest bar name is:',
        get_bar_name(get_smallest_bar(bars_list))
    )

    longitude = coordinate_to_float(input('Input your longitude: '))
    latitude = coordinate_to_float(input('Input your latitude: '))
    if not (longitude and latitude):
        sys.exit('Wrong coordinates')

    print(
        'Closest bar name is:',
        get_bar_name(get_closest_bar(bars_list, longitude, latitude))
    )
