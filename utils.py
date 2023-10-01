from json import load


def get_data():
    with open('operations.json', 'r', encoding='utf8') as file:
        data = load(file)
    return data


def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data



