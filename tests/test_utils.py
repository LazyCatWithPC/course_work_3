import utils


def test_get_data():
    data = utils.get_data()
    assert isinstance(data, list)


def test_get_last_values(test_data):
    data = utils.get_last_values(test_data)
    assert [x['date'] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']


def test_formate_info_and_hide_number():
    assert utils.formate_info_and_hide_number('Счет 41421565395219882431') == 'Счет **2431'
    assert utils.formate_info_and_hide_number('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert utils.formate_info_and_hide_number('') == ''


def test_get_formatted_data(test_data):
    data = utils.get_formatted_data(test_data)
    assert data[0] == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.'
