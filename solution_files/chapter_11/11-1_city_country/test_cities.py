from city_functions import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    clementi_singapore = city_country('clementi', 'singapore')
    hongkong_china = city_country('hong kong', 'china')
    assert santiago_chile == 'Santiago, Chile'
    assert clementi_singapore == 'Clementi, Singapore'
    assert hongkong_china == 'Hong Kong, China'