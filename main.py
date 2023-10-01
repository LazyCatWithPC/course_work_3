import utils


def main():
    data = utils.get_data()
    data = utils.filter_data(data)
    data = utils.get_last_values(data)
    data = utils.get_formatted_data(data)
    print('Вывожу транзакции...\n')
    for row in data:
        print(row, end='\n\n')


if __name__ == '__main__':
    main()
