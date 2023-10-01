from json import load
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf8') as file:
        data = load(file)
    return data


def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def get_last_values(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)[:5]
    return data


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], __format="%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = data["description"]
        from_info = ''
        if 'from' in row:
            from_info = data['from'] + ' ->'
        recipient = data['to']
        operations_amount = f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{from_info} {recipient}
{operations_amount}""")
    return formatted_data
