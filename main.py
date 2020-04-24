from starsystem import StarSystem


def functional():
    test_planet = StarSystem("Qewra", "0105", "D46668A-3", "SG", "Ag Lt Ni Ri A")
    test_planet_two = StarSystem("Zudqe", "0408", "A200657-14", "NTC", "Ht Na Ni Va")
    print(test_planet)
    print(test_planet_two)

    print(test_planet.get_passengers_base_dm(test_planet_two))
    print(test_planet.get_passengers(test_planet_two, 12))

    print(test_planet.get_freight_base_dm(test_planet_two))
    print(test_planet.get_freight(test_planet_two))

    print(test_planet.get_mail_dm(test_planet_two, True, 3, 2))
    print(test_planet.has_mail(test_planet_two, True, 3, 2, 8))

    print(test_planet.get_session_purchase_goods())
    print(test_planet.buy_goods("Basic Ore", 15))
    print(test_planet_two.sell_goods("Basic Ore", 15))

functional()

