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


def formate_info_and_hide_number(data):
    if data != '':
        counter = 0
        hidden_number = ''
        data = data.split()
        number = data[-1]
        if len(number) == 16:
            for i in number:
                counter += 1
                if 6 < counter < 13:
                    hidden_number += '*'
                else:
                    hidden_number += i
                if counter % 4 == 0:
                    hidden_number += ' '
            hidden_number = hidden_number[:-1]
        else:
            hidden_number = '**' + number[-4:]
        data[-1] = hidden_number
        new_data = ' '.join(data)
        return new_data


def get_formatted_data(data):
    counter = 0
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = data[counter]["description"]
        operations_amount = f"{data[counter]['operationAmount']['amount']} {data[counter]['operationAmount']['currency']['name']}"
        from_data = ''
        if 'from' in row:
            from_data = formate_info_and_hide_number(data[counter]['from']) + ' -> '
        to_data = formate_info_and_hide_number(data[counter]['to'])


        formatted_data.append(f"""\
{date} {description}
{from_data}{to_data}
{operations_amount}""")
        counter += 1
    return formatted_data
