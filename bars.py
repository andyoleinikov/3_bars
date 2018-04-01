import json
import os
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return False


def get_biggest_bar(bars_list):
    biggest_bar = max(bars_list, key=lambda item:
                      item['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_list):
    smallest_bar = min(bars_list, key=lambda item:
                       item['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars_list, longitude, latitude):
    biggest_distance = 40000
    closest_bar = ''
    for bar in bars_list:
        distance = ((longitude - bar['geometry']['coordinates'][0])**2 +
                    (latitude - bar['geometry']['coordinates'][1])**2)**(1 / 2)
        if distance < biggest_distance:
            biggest_distance = distance
            closest_bar = bar
    return closest_bar


def coordinate_to_float(coordinate_str):
    try:
        coordinate = float(coordinate_str)
        return coordinate
    except ValueError:
        return False


if __name__ == '__main__':
    filepath = 'bars.json'
    if len(sys.argv) > 1:
        filepath = sys.argv[1]

    bars_list = load_data(filepath)['features']
    if bars_list:

        print('Biggest bar is:', get_biggest_bar(bars_list))
        print('Smallest bar is:', get_smallest_bar(bars_list))

        longitude = coordinate_to_float(input('Input your longitude: '))
        latitude = coordinate_to_float(input('Input your latitude: '))

        if longitude and latitude:
            print('Closest bar is:',
                  get_closest_bar(bars_list, longitude, latitude))

        else:
            print('Wrong coordinates')

    else:
        print('Wrong file or path')
