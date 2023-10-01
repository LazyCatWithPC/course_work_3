from json import load
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf8') as file:
        data = load(file)
    return data


def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data



