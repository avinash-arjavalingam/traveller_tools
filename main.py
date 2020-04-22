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

functional()

