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


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No path specified')
        exit()

    filepath = sys.argv[1]
    bars_dict = load_data(filepath)
    if bars_dict is None:
        print('Wrong file')
        exit()

    bars_list = bars_dict['features']

    print(
        'Biggest bar name is:',
        get_biggest_bar(bars_list)['properties']['Attributes']['Name']
    )

    print(
        'Smallest bar name is:',
        get_smallest_bar(bars_list)['properties']['Attributes']['Name']
    )

    longitude = coordinate_to_float(input('Input your longitude: '))
    latitude = coordinate_to_float(input('Input your latitude: '))
    if not (longitude and latitude):
        print('Wrong coordinates')
        exit()

    print(
        'Closest bar name is:',
        get_closest_bar(bars_list, longitude, latitude)
        ['properties']['Attributes']['Name']
    )
