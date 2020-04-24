import random


class StarSystem:

    base_map = {'N': "Naval Base", 'S': "Scout Base", 'R': "Research Base", 'T': "TAS Hostel",
                'C': "Imperial Consulate", 'P': "Pirate Base", 'G': "Gas Giant"}

    trade_codes_map = {"Ag": "Agricultural", "As": "Asteroid", "Ba": "Barren", "De": "Desert", "Fl": "Fluid Oceans",
                       "Ga": "Garden", "Hi": "High Population", "Ht": "High Technology", "Ic": "Ice-Capped",
                       "In": "Industrial", "Lo": "Low Population", "Lt": "Low Technology", "Na": "Non-Agricultural",
                       "Ni": "Non-Industrial", "Po": "Poor", "Ri": "Rich", "Va": "Vacuum", "Wa": "Water World",
                       "A": "Amber Zone", "R": "Red Zone"}

    trade_codes_mod_table_colums = ["Current passenger traffic", "Destination passenger traffic",
                                    "Current freight traffic", "Destination freight traffic"]

    trade_codes_mod_table = {"Agricultural": [0, 0, 2, 1], "Asteroid": [1, -1, -3, 1],
                             "Barren": [-5, -5, -1000, -5], "Desert": [-1, -1, -3, 0],
                             "Fluid Oceans": [0, 0, -3, 0], "Garden": [2, 2, 2, 1], "High Population": [0, 4, 2, -1],
                             "Ice-Capped": [1, -1, -3, 0], "Industrial": [2, 1, 3, 2], "Low Population": [0, -4, -5, 0],
                             "Non-Agricultural": [0, 0, -3, 1], "Non-Industrial": [0, -1, -3, 1],
                             "Poor": [-2, -1, -3, -3], "Rich": [-1, 2, 2, 2], "Water World": [0, 0, -3, 0],
                             "Amber Zone": [2, -2, 5, -5], "Red Zone": [4, -4, -5, -1000]}

    trade_goods_default_available = {"Agricultural": {"Biochemicals", "Live Animals", "Luxury Consumables", "Textiles",
                                                      "Uncommon Raw Materials", "Wood", "Illegal Biochemicals",
                                                      "Illegal Luxuries"},
                                     "Asteroid": {"Crystals and Gems", "Pharmaceuticals", "Precious Metals",
                                                  "Radioactives", "Uncommon Ore", "Illegal Drugs"},
                                     "Desert": {"Crystals and Gems", "Petrochemicals", "Pharmaceuticals",
                                                "Precious Metals", "Radioactives", "Spices", "Uncommon Raw Materials",
                                                "Illegal Drugs", "Illegal Luxuries"},
                                     "Fluid Oceans": {"Petrochemicals", "Precious Metals"},
                                     "Garden": {"Live Animals", "Luxury Consumables", "Spices", "Wood"},
                                     "High Population": {"Luxury Goods", "Medical Supplies", "Pharmaceuticals",
                                                         "Illegal Drugs"},
                                     "High Technology": {"Advanced Electronics", "Advanced Machine Parts",
                                                         "Advanced Manufactured Goods", "Advanced Weapons",
                                                         "Advanced Vehicles", "Cybernetics", "Medical Supplies",
                                                         "Robots", "Vehicles", "Illegal Weapons"},
                                     "Ice-Capped": {"Crystals and Gems", "Petrochemicals", "Precious Metals",
                                                    "Uncommon Ore"},
                                     "Industrial": {"Advanced Electronics", "Advanced Machine Parts",
                                                    "Advanced Manufactured Goods", "Advanced Weapons",
                                                    "Advanced Vehicles", "Polymers", "Robots", "Vehicles",
                                                    "Illegal Weapons "},
                                     "Low Population": {"Radioactives"},
                                     "Non-Industrial": {"Textiles"},
                                     "Water World": {"Biochemicals", "Luxury Consumables", "Petrochemicals",
                                                     "Pharmaceuticals", "Spices", "Uncommon Raw Materials",
                                                     "Illegal Biochemicals", "Illegal Drugs", "Illegal Luxuries"}}

    trade_goods_map = {11: "Basic Electronics", 12: "Basic Machine Parts", 13: "Basic Manufactured Goods",
                       14: "Basic Raw Materials", 15: "Basic Consumables", 16: "Basic Ore", 21: "Advanced Electronics",
                       22: "Advanced Machine Parts", 23: "Advanced Manufactured Goods", 24: "Advanced Weapons",
                       25: "Advanced Vehicles", 26: "Biochemicals", 31: "Crystals and Gems", 32: "Cybernetics",
                       33: "Live Animals", 34: "Luxury Consumables", 35: "Luxury Goods", 36: "Medical Supplies",
                       41: "Petrochemicals", 42: "Pharmaceuticals", 43: "Polymers", 44: "Precious Metals",
                       45: "Radioactives", 46: "Robots", 51: "Spices", 52: "Textiles", 53: "Uncommon Ore",
                       54: "Uncommon Raw Materials", 55: "Wood", 56: "Vehicles", 61: "Illegal Biochemicals",
                       62: "Illegal Cybernetics", 63: "Illegal Drugs", 64: "Illegal Luxuries", 65: "Illegal Weapons",
                       66: "Exotics"}

    trade_goods_mod = {"Basic Electronics": 10, "Basic Machine Parts": 10, "Basic Manufactured Goods": 10,
                       "Basic Raw Materials": 10, "Basic Consumables": 10, "Basic Ore": 10, "Advanced Electronics": 5,
                       "Advanced Machine Parts": 5, "Advanced Manufactured Goods": 5, "Advanced Weapons": 5,
                       "Advanced Vehicles": 5, "Biochemicals": 5, "Crystals and Gems": 5, "Cybernetics": 1,
                       "Live Animals": 10, "Luxury Consumables": 10, "Luxury Goods": 1, "Medical Supplies": 5,
                       "Petrochemicals": 10, "Pharmaceuticals": 1, "Polymers": 10, "Precious Metals": 1,
                       "Radioactives": 1, "Robots": 5, "Spices": 5, "Textiles": 10, "Uncommon Ore": 10,
                       "Uncommon Raw Materials": 10, "Wood": 10, "Vehicles": 10, "Illegal Biochemicals": 5,
                       "Illegal Cybernetics": 1, "Illegal Drugs": 1, "Illegal Luxuries": 1, "Illegal Weapons": 5,
                       "Exotics": 1}

    trade_goods_pri = {"Basic Electronics": 10000, "Basic Machine Parts": 10000, "Basic Manufactured Goods": 10000,
                       "Basic Raw Materials": 5000, "Basic Consumables": 2000, "Basic Ore": 1000,
                       "Advanced Electronics": 100000, "Advanced Machine Parts": 75000,
                       "Advanced Manufactured Goods": 100000, "Advanced Weapons": 150000,
                       "Advanced Vehicles": 180000, "Biochemicals": 50000, "Crystals and Gems": 20000,
                       "Cybernetics": 250000, "Live Animals": 10000, "Luxury Consumables": 20000,
                       "Luxury Goods": 200000, "Medical Supplies": 50000, "Petrochemicals": 10000,
                       "Pharmaceuticals": 100000, "Polymers": 7000, "Precious Metals": 50000,
                       "Radioactives": 1000000, "Robots": 400000, "Spices": 6000, "Textiles": 3000,
                       "Uncommon Ore": 5000, "Uncommon Raw Materials": 20000, "Wood": 1000, "Vehicles": 15000,
                       "Illegal Biochemicals": 50000, "Illegal Cybernetics": 250000, "Illegal Drugs": 100000,
                       "Illegal Luxuries": 50000, "Illegal Weapons": 150000, "Exotics": 1000000}

    trade_goods_pur = {"Basic Electronics": {"Industrial": 2, "High Technology": 3, "Rich": 1},
                       "Basic Machine Parts": {"Non-Agricultural": 2, "Industrial": 5},
                       "Basic Manufactured Goods": {"Non-Agricultural": 2, "Industrial": 5},
                       "Basic Raw Materials": {"Agricultural": 3, "Garden": 2},
                       "Basic Consumables": {"Agricultural": 3, "Water World": 2, "Garden": 1, "Asteroid": -4},
                       "Basic Ore": {"Asteroid": 4, "Ice Capped": 0},
                       "Advanced Electronics": {"Industrial": 2, "High Technology": 3},
                       "Advanced Machine Parts": {"Industrial": 2, "High Technology": 1},
                       "Advanced Manufactured Goods": {"Industrial": 1, "High Technology": 0},
                       "Advanced Weapons": {"Industrial": 0, "High Technology": 2},
                       "Advanced Vehicles": {"Industrial": 0, "High Technology": 2},
                       "Biochemicals": {"Agricultural": 1, "Water World": 2},
                       "Crystals and Gems": {"Asteroid": 2, "Desert": 1, "Ice Capped": 1},
                       "Cybernetics": {"High Technology": 0},
                       "Live Animals": {"Agricultural": 2, "Garden": 0},
                       "Luxury Consumables": {"Agricultural": 2, "Garden": 0, "Water World": 1},
                       "Luxury Goods": {"High Population": 0},
                       "Medical Supplies": {"High Technology": 2, "High Population": 0},
                       "Petrochemicals": {"Desert": 2, "Fluid Oceans": 0, "Ice-Capped": 0, "Water World": 0},
                       "Pharmaceuticals": {"Asteroid": 2, "Desert": 0, "High Population": 1, "Water World": 0},
                       "Polymers": {"Industrial": 0},
                       "Precious Metals": {"Asteroid": 3, "Desert": 1, "Ice-Capped": 2, "Fluid Oceans": 0},
                       "Radioactives": {"Asteroid": 2, "Desert": 0, "Low Population": -4},
                       "Robots": {"Industrial": 0},
                       "Spices": {"Garden": 0, "Desert": 2, "Water World": 0},
                       "Textiles": {"Agricultural": 7, "Non-Industrial": 0},
                       "Uncommon Ore": {"Asteroid": 4, "Ice-Capped": 0},
                       "Uncommon Raw Materials": {"Agricultural": 2, "Desert": 0, "Water World": 1},
                       "Wood": {"Agricultural": 6, "Garden": 0},
                       "Vehicles": {"Industrial": 2, "High Technology": 1},
                       "Illegal Biochemicals": {"Agricultural": 0, "Water World": 2},
                       "Illegal Cybernetics": {"High Technology": 0},
                       "Illegal Drugs": {"Asteroid": 0, "Desert": 0, "Garden": 0, "Water World": 0},
                       "Illegal Luxuries": {"Agricultural": 2, "Garden": 0, "Water World": 1},
                       "Illegal Weapons": {"Industrial": 0, "High Technology": 2},
                       "Exotics": {}}

    trade_goods_sal = {"Basic Electronics": {"Non-Industrial": 2, "Low Technology": 1, "Poor": 1},
                       "Basic Machine Parts": {"Agricultural": 2, "Non-Industrial": 3},
                       "Basic Manufactured Goods": {"High Population": 2, "Non-Industrial": 3},
                       "Basic Raw Materials": {"Industrial": 2, "Poor": 2},
                       "Basic Consumables": {"Asteroid": 1, "Fluid Oceans": 1, "Ice Capped": 1, "High Population": 1},
                       "Basic Ore": {"Industrial": 3, "Non-Industrial": 1},
                       "Advanced Electronics": {"Non-Industrial": 1, "Rich": 2, "Asteroid": 3},
                       "Advanced Machine Parts": {"Non-Industrial": 1, "Asteroid": 2},
                       "Advanced Manufactured Goods": {"High Population": 1, "Rich": 2},
                       "Advanced Weapons": {"Poor": 1, "Amber Zone": 2, "Red Zone": 4},
                       "Advanced Vehicles": {"Asteroid": 2, "Rich": 2},
                       "Biochemicals": {"Industrial": 2},
                       "Crystals and Gems": {"Industrial": 3, "Rich": 2},
                       "Cybernetics": {"Asteroid": 1, "Ice-Capped": 1, "Rich": 2},
                       "Live Animals": {"Low Population": 3},
                       "Luxury Consumables": {"Rich": 2, "High Population": 2},
                       "Luxury Goods": {"Rich": 4},
                       "Medical Supplies": {"Industrial": 2, "Poor": 1, "Rich": 1},
                       "Petrochemicals": {"Industrial": 2, "Agricultural": 1, "Low Technology": 2},
                       "Pharmaceuticals": {"Rich": 2, "Low Technology": 1},
                       "Polymers": {"Rich": 2, "Non-Industrial": 1},
                       "Precious Metals": {"Rich": 3, "Industrial": 2, "High Technology": 1},
                       "Radioactives": {"Industrial": 3, "High Technology": 1, "Non-Industrial": -2,
                                        "Agricultural": -3},
                       "Robots": {"Agricultural": 2, "High Technology": 1},
                       "Spices": {"High Population": 2, "Rich": 3, "Poor": 3},
                       "Textiles": {"High Population": 3, "Non-Agricultural": 2},
                       "Uncommon Ore": {"Industrial": 3, "Non-Industrial": 1},
                       "Uncommon Raw Materials": {"Industrial": 2, "High Technology": 1},
                       "Wood": {"Rich": 2, "Industrial": 1},
                       "Vehicles": {"Non-Industrial": 2, "High Population": 1},
                       "Illegal Biochemicals": {"Industrial": 6},
                       "Illegal Cybernetics": {"Asteroid": 4, "Ice-Capped": 4, "Rich": 8, "Amber Zone": 6,
                                               "Red Zone": 6},
                       "Illegal Drugs": {"Rich": 6, "High Population": 6},
                       "Illegal Luxuries": {"Rich": 6, "High Population": 4},
                       "Illegal Weapons": {"Poor": 6, "Amber Zone": 8, "Red Zone": 10},
                       "Exotics": {}}

    passenger_roll_table_columns = ["Low Passages", "Middle Passages", "High Passages"]

    passenger_roll_table = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            [[2, 0, 6], [1, 0, 2], [0, 0, 0]],
                            [[2, 0, 0], [1, 0, 0], [1, 1, 0]],
                            [[2, 0, 0], [2, 1, 0], [2, 2, 0]],
                            [[3, 1, 0], [2, 1, 0], [2, 1, 0]],
                            [[3, 1, 0], [3, 2, 0], [2, 1, 0]],
                            [[3, 0, 0], [3, 2, 0], [3, 2, 0]],
                            [[3, 0, 0], [3, 1, 0], [3, 2, 0]],
                            [[4, 0, 0], [3, 1, 0], [3, 1, 0]],
                            [[4, 0, 0], [3, 0, 0], [3, 1, 0]],
                            [[5, 0, 0], [3, 0, 0], [3, 1, 0]],
                            [[5, 0, 0], [4, 0, 0], [3, 0, 0]],
                            [[6, 0, 0], [4, 0, 0], [3, 0, 0]],
                            [[6, 0, 0], [4, 0, 0], [4, 0, 0]],
                            [[7, 0, 0], [5, 0, 0], [4, 0, 0]],
                            [[8, 0, 0], [5, 0, 0], [4, 0, 0]],
                            [[9, 0, 0], [6, 0, 0], [5, 0, 0]]]

    freight_roll_table_columns = ["Incidental", "Minor", "Major"]

    freight_roll_table = [[[0, 0], [0, 0], [0, 0]],
                          [[0, 0], [1, -4], [1, -4]],
                          [[0, 0], [1, -1], [1, -2]],
                          [[0, 0], [1, 0], [1, -1]],
                          [[0, 0], [1, 1], [1, 0]],
                          [[0, 0], [1, 2], [1, 1]],
                          [[0, 0], [1, 3], [1, 2]],
                          [[0, 0], [1, 4], [1, 3]],
                          [[0, 0], [1, 5], [1, 4]],
                          [[1, -2], [1, 6], [1, 5]],
                          [[1, 0], [1, 7], [1, 6]],
                          [[1, 1], [1, 8], [1, 7]],
                          [[1, 2], [1, 9], [1, 8]],
                          [[1, 3], [1, 10], [1, 9]],
                          [[1, 4], [1, 12], [1, 10]],
                          [[1, 5], [1, 14], [1, 11]],
                          [[1, 6], [1, 16], [1, 12]]]

    modified_price_table_columns = ["Purchase Price", "Sale Price"]

    modified_price_table_plus_one = [[4.0, 0.25], [3.0, 0.45], [2.0, 0.5], [1.75, 0.55], [1.5, 0.6], [1.35, 0.65],
                                     [1.25, 0.75], [1.2, 0.8], [1.15, 0.85], [1.1, 0.9], [1.05, 0.95], [1, 1],
                                     [0.95, 1.05], [0.9, 1.1], [0.85, 1.15], [0.8, 1.2], [0.75, 1.25], [0.7, 1.35],
                                     [0.65, 1.5], [0.55, 1.75], [0.5, 2.0], [0.45, 3.0], [0.25, 4.0]]

    starport_quality_map = {'A': "Excellent", 'B': "Good", 'C': "Routine", 'D': "Poor", 'E': "Frontier",
                            'X': "No Starport"}

    size_table = [800, 1600, 3200, 4800, 6400, 8000, 9600, 11200, 12800, 14400, 16000]

    distance_to_time_map = [[1000, 633], [10000, 2000], [100000, 6300], [300000, 10980], [400000, 12660],
                              [1000000, 19980], [10000000, 63360], [30000000, 109512], [4500000, 134280],
                              [100000000, 200160], [150000000, 244800], [255000000, 319320], [600000000, 489960],
                              [900000000, 600120], [1000000000, 630720]]

    starport_info_columns = ["Berthing Cost 1d6 Multiplier", "Fuel Available", "Facilities"]

    starport_info_map = {'A': [1000, "Refined", ["Shipyard (all)", "Repair"]],
                         'B': [500, "Refined", ["Shiyard (spacecraft)", "Repair"]],
                         'C': [100, "Unrefined", ["Shiyard (small craft)", "Repair"]],
                         'D': [10, "Unrefined", ["Limited Repair"]],
                         'E': [0, "None", ["None"]],
                         'X': [0, "None", ["None"]]}

    atmosphere_table = [["None"], ["Trace"], ["Very Thin", "Tainted"], ["Very Thin"], ["Thin", "Tainted"], ["Thin"],
                        ["Standard"], ["Standard", "Tainted"], ["Dense"], ["Dense", "Tainted"], ["Exotic"],
                        ["Corrosive"], ["Insidious"], ["Dense", "High"], ["Thin", "Low"], ["Unusual"]]

    atmosphere_columns = ["Examples", "Pressure", "Survival Gear Required"]

    atmosphere_map = [["Moon", "0.00", "Vacc Suit"], ["Mars", "0.001 to 0.09", "Vacc Suit"],
                      ["None", "0.1 to 0.42", "Respirator, Filter"], ["None", "0.1 to 0.42", "Respirator"],
                      ["None", "0.43 to 0.7", "Filter"], ["None", "0.43 to 0.7", "None"],
                      ["Earth", "0.71–1.49", "None"], ["None", "0.71–1.49", "Filter"],
                      ["None", "1.5 to 2.49", "None"], ["None", "1.5 to 2.49", "Filter"],
                      ["None", "Varies", "Air Supply"], ["Venus", "Varies", "Vacc Suit"],
                      ["None", "Varies", "Vacc Suit"], ["None", "2.5+", "None"],
                      ["None", "0.5 or less", "None"], ["None", "Varies", "Varies"]]

    atmosphere_description_map = {"Tainted": "Tainted atmospheres contain some element that is harmful to "
                                             "humans, such as an unusually high proportion of carbon dioxide. A "
                                             "character who breathes a tainted atmosphere without a filter will "
                                             "suffer 1d6 damage every few minutes (or hours, depending on the "
                                             "level of taint). ",
                                  "Exotic": "An exotic atmosphere is unbreathable by humans, but is not otherwise "
                                            "hazardous. A character needs an air supply to breath in an exotic "
                                            "atmosphere. ",
                                  "Corrosive": "Corrosive atmospheres are highly dangerous. A character who "
                                               "breathes in a corrosive atmosphere will suffer 1d6 damage each round. ",
                                  "Insidious": "An insidious atmosphere is like a corrosive one, but it is so corrosive"
                                               " that it attacks equipment as well. The chief danger in an insidious "
                                               "atmosphere is that the toxic gases will destroy the seals and filters "
                                               "on the character’s protective gear. An insidious atmosphere worms its "
                                               "way past protection after 2d6 hours on average, although vigilant "
                                               "maintenance or advanced protective gear can prolong survival times.",
                                  "Dense, High": "These worlds have thick N2/O2 atmospheres, but their mean surface "
                                                 "pressure is too high to support unprotected human life (high "
                                                 "pressure nitrogen and oxygen are deadly to humans). However, "
                                                 "pressure naturally decreases with increasing altitude, so if there "
                                                 "are highlands at the right altitude the pressure may drop enough to "
                                                 "support human life. Alternatively, there may not be any topography "
                                                 "high enough for humans to inhabit, necessitating floating gravitic "
                                                 "or dirigible habitats or sealed habitats on the surface. ",
                                  "Thin, Low": "The opposite of the Dense, High atmosphere, these massive worlds have "
                                               "thin N2/O2 atmospheres that settle in the lowlands and depressions and "
                                               "are only breathable there – the pressure drops off so rapidly with "
                                               "altitude that the highest topographic points of the surface may be "
                                               "close to vacuum.",
                                  "Unusual": "An Unusual atmosphere is a catchall term for an atmosphere that behaves "
                                             "in a strange manner. Examples include ellipsoidal atmospheres, which are "
                                             "thin at the poles and dense at the equator; Panthalassic worlds composed "
                                             "of a rocky core surrounded by a water layer hundreds of kilometres "
                                             "thick; worlds wracked by storms so intense that that the local air "
                                             "pressure changes from dense to thin depending on the current weather; "
                                             "and other planets with unusual and hazardous atmospheric conditions."}

    hydrographic_percentage_table = ["0%–5%", "6%–15%", "16%–25%", "26%–35%", "36%–45%", "46%–55%", "56%–65%",
                                     "66%–75%", "76%–85%", "86%–95%", "96–100%"]

    population_table = ["None", "Few", "Hundreds", "Thousands", "Tens of thousands", "Hundreds of thousands",
                        "Millions", "Tens of millions", "Hundreds of millions", "Billions", "Tens of billions",
                        "Hundreds of billions", "Trillions"]

    government_table = ["None", "Company/corporation", "Participating democracy", "Self-perpetuating oligarchy",
                        "Representative democracy", "Feudal technocracy", "Captive government", "Balkanisation",
                        "Civil service bureaucracy", "Impersonal Bureaucracy", "Charismatic dictator",
                        "Non-charismatic leader", "Charismatic oligarchy", "Religious dictatorship"]

    law_level_columns = ["Weapons", "Drugs", "Information", "Technology", "Travellers", "Psionics"]
    law_level_table = [["None", "None", "None", "None", "None", "None"],
                       ["Poison gas, explosives, undetectable weapons, WMD",
                        "Highly addictive and dangerous narcotics", "Intellect programs",
                        "Dangerous technologies such as nanotechnology",
                        "Visitors must contact planetary authorities by radio, "
                        "landing is permitted anywhere", "Dangerous talents must be registered."],
                       ["Portable energy weapons (except ship-mounted weapons)", "Highly addictive narcotics",
                        "Agent programs", "Alien technology",
                        "Visitors must report passenger manifest, landing is permitted anywhere",
                        "All psionic powers must be registered; use of dangerous powers forbidden."],
                       ["Heavy weapons", "Combat drugs", "Intrusion programs", "TL 15 items",
                        "Landing only at starport or other authorised sites",
                        "Use of telepathy restricted to government approved telepaths"],
                       ["Light assault weapons and submachine guns", "Addictive narcotics", "Security programs",
                        "TL 13 items", "Landing only at starport", "Use of teleportation and clairvoyance restricted"],
                       ["Personal concealable weapons", "Anagathics", "Expert programs", "TL 11 items",
                        "Citizens must register offworld travel, visitors must register all business",
                        "Use of all psionic powers restricted to government psionicists"],
                       ["All firearms except shotguns and stunners; carrying weapons discouraged",
                        "Fast and Slow drugs", "Recent news from offworld", "TL 9 items",
                        "Visits discouraged; excessive contact with citizens forbidden",
                        "Possession of psionic drugs banned"],
                       ["Shotguns", "All narcotics",
                       "Library programs, unfiltered data about other worlds. Free speech curtailed.",
                       "TL 7 items", "Citizens may not leave planet; visitors may not leave starport",
                        "Use of psionics forbidden"],
                       ["All bladed weapons, stunners", "Medicinal drugs",
                        "Information technology, any non-critical data from offworld, personal media.",
                        "TL 5 items", "Landing permitted only to imperial agents", "Psionic-related technology banned"],
                       ["Any weapons", "All drugs", "Any data from offworld. No free press", "TL 3 items",
                        "No offworlders permitted", "All psionics"]]

    def __init__(self, name, location, characteristics, bases=None, trade_codes=None, faction=None):
        self.name = name
        self.location = location
        self.characteristics = characteristics
        self.starport_quality = (characteristics[0], self.starport_quality_map[characteristics[0]])
        self.size = (self.hex_char_to_int(1), self.hex_char_to_istic(1, self.size_table))
        self.atmosphere_type = (self.hex_char_to_int(2), self.hex_char_to_istic(2, self.atmosphere_table))
        self.hydrographic_percentage = (self.hex_char_to_int(3),
                                        self.hex_char_to_istic(3, self.hydrographic_percentage_table))
        self.population = (self.hex_char_to_int(4), self.hex_char_to_istic(4, self.population_table))
        self.government_type = (self.hex_char_to_int(5), self.hex_char_to_istic(5, self.government_table))
        self.law_level = self.hex_char_to_int(6)
        self.tech_level = int(self.characteristics[8:])

        self.bases = []
        if bases is not None:
            for base_char in list(bases):
                self.bases.append(self.base_map[base_char])
            self.bases = set(self.bases)
        else:
            self.bases = None

        self.trade_codes = []
        if trade_codes is not None:
            for trade_code in trade_codes.split():
                self.trade_codes.append(self.trade_codes_map[trade_code])
            self.trade_codes = set(self.trade_codes)
        else:
            self.trade_codes = None

        self.faction = faction

        self.default_trade_goods = {"Basic Electronics", "Basic Machine Parts", "Basic Manufactured Goods",
                                    "Basic Raw Materials", "Basic Consumables", "Basic Ore"}
        if self.trade_codes is not None:
            for code in self.trade_codes:
                if code in self.trade_goods_default_available.keys():
                    self.default_trade_goods = self.default_trade_goods.union(self.trade_goods_default_available[code])

        self.default_trade_goods_dm_map = {}

        for good in self.default_trade_goods:
            self.default_trade_goods_dm_map[good] = self.good_trade_dm(good, self.trade_goods_pur) \
                                                    - self.good_trade_dm(good, self.trade_goods_sal)

        self.sell_goods_dm = {}
        for good in self.trade_goods_mod.keys():
            self.sell_goods_dm[good] = self.good_trade_dm(good, self.trade_goods_sal) \
                                       - self.good_trade_dm(good, self.trade_goods_pur)

        self.session_purchase_goods = {}

    def hex_char_to_int(self, index):
        return int((self.characteristics[index]), 16)

    def hex_char_to_istic(self, index, istic_list):
        return istic_list[self.hex_char_to_int(index)]

    def get_passengers_base_dm(self, other_planet):
        dm = self.population[0]

        if self.trade_codes is not None:
            for code in self.trade_codes:
                if code in self.trade_codes_mod_table.keys():
                    dm += self.trade_codes_mod_table[code][0]

        if other_planet.trade_codes is not None:
            for code in other_planet.trade_codes:
                if code in other_planet.trade_codes_mod_table.keys():
                    dm += other_planet.trade_codes_mod_table[code][1]

        dm = max(0, dm)

        return dm

    def get_passengers(self, other_planet, carouse_check=8):
        dm = self.get_passengers_base_dm(other_planet)
        effect = int((carouse_check - 8) / 2)
        dm += effect
        dm = min(dm, 16)

        pass_pos = self.passenger_roll_table[dm]
        return {"Low Passages": self.pass_rolling(pass_pos[0]), "Middle Passages": self.pass_rolling(pass_pos[1]),
                "High Passages": self.pass_rolling(pass_pos[2])}

    def get_freight_base_dm(self, other_planet):
        dm = other_planet.population[0]

        if self.trade_codes is not None:
            for code in self.trade_codes:
                if code in self.trade_codes_mod_table.keys():
                    dm += self.trade_codes_mod_table[code][2]

        if other_planet.trade_codes is not None:
            for code in other_planet.trade_codes:
                if code in other_planet.trade_codes_mod_table.keys():
                    dm += other_planet.trade_codes_mod_table[code][3]

        tech_mod = min(abs(self.tech_level - other_planet.tech_level), 5)
        dm -= tech_mod

        dm = max(0, dm)

        return dm

    def get_freight(self, other_planet):
        dm = self.get_freight_base_dm(other_planet)
        dm = min(dm, 16)

        freight_pos = self.freight_roll_table[dm]
        inc_lots = self.freight_rolling(freight_pos[0])
        # print("Incidental Lots: " + str(inc_lots))
        min_lots = self.freight_rolling(freight_pos[1])
        # print("Minor Lots: " + str(min_lots))
        maj_lots = self.freight_rolling(freight_pos[2])
        # print("Major Lots: " + str(maj_lots))
        cargoes = {}
        self.lot_to_cargo(inc_lots, 1, cargoes)
        self.lot_to_cargo(min_lots, 5, cargoes)
        self.lot_to_cargo(maj_lots, 10, cargoes)

        cargo_list = []
        for cargo_weight in sorted(cargoes.keys()):
            cargo_list.append(str(cargoes[cargo_weight]) + " lots of " + str(cargo_weight) + " tons")

        return cargo_list

    def get_mail_dm(self, other_planet, armed, navy_scout_rank, soc_stand_dm):
        mail_dm = 0
        freight_dm = self.get_freight_base_dm(other_planet)
        if freight_dm <= -10:
            mail_dm = -2
        elif (freight_dm <= -5) and (freight_dm >= -9):
            mail_dm = -1
        elif (freight_dm <= 4) and (freight_dm >= -4):
            mail_dm = 0
        elif (freight_dm <= 9) and (freight_dm >= 5):
            mail_dm = 1
        elif freight_dm >= 10:
            mail_dm = 2

        if armed:
            mail_dm += 2

        mail_dm = mail_dm + navy_scout_rank + soc_stand_dm

        if self.tech_level <= 5:
            mail_dm -= 4

        return mail_dm

    def has_mail(self, other_planet, armed, navy_scout_rank, soc_stand_dm, mail_roll):
        mail_dm = self.get_mail_dm(other_planet, armed, navy_scout_rank, soc_stand_dm)

        if mail_roll + mail_dm >= 12:
            return True
        else:
            return False

    def good_trade_dm(self, good, trade_map):
        good_pur_dm = trade_map[good]
        changed = False
        max_pur_dm = float('-inf')
        if self.trade_codes is not None:
            for code in self.trade_codes:
                if code in good_pur_dm.keys():
                    code_pur_mod = good_pur_dm[code]
                    if code_pur_mod > max_pur_dm:
                        changed = True
                        max_pur_dm = code_pur_mod

        if not changed:
            max_pur_dm = 0
        return max_pur_dm

    def get_session_purchase_goods(self):
        if self.session_purchase_goods != {}:
            return self.session_purchase_goods
        else:
            temp_session_goods = {}
            session_goods = {}
            for good, dm in self.default_trade_goods_dm_map.items():
                weight = random.randint(1, 6) * self.trade_goods_mod[good]
                temp_session_goods[good] = [weight, self.trade_goods_pri[good], dm]
            num_extra = random.randint(1, 6)
            for i in range(num_extra):
                sixty_six_roll = (random.randint(1, 6) * 10) + random.randint(1, 6)
                added_good = self.trade_goods_map[sixty_six_roll]
                added_weight = random.randint(1, 6) * self.trade_goods_mod[added_good]
                if added_good in temp_session_goods.keys():
                    temp_session_goods[added_good][0] = temp_session_goods[added_good][0] + added_weight
                else:
                    temp_session_goods[added_good] = [added_weight, self.trade_goods_pri[added_good],
                                                      self.good_trade_dm(added_good, self.trade_goods_pur)
                                                      - self.good_trade_dm(added_good, self.trade_goods_sal)]

            for final_good, vals in temp_session_goods.items():
                session_goods[final_good] = str(vals[0]) + " tons at " + str(vals[1]) \
                                            + " per ton at a purchase DM of " + str(vals[2])

            self.session_purchase_goods = temp_session_goods

            return session_goods

    def clear_session(self):
        self.session_purchase_goods = {}

    def buy_goods(self, good, broker_roll):
        if good not in self.session_purchase_goods.keys():
            return "Not available! Idiot"
        good_value = self.session_purchase_goods[good]
        true_roll = broker_roll + good_value[2]
        true_roll = max(true_roll, -1)
        true_roll = min(true_roll, 21)
        true_roll += 1
        price_change = self.modified_price_table_plus_one[true_roll][0]

        new_price = price_change * good_value[1]

        ret_str = "At a " + str(int(price_change * 100)) + "% price change, there are " + str(good_value[0]) + \
                  " tons of " + good + " at " + str(int(new_price)) + " per ton"
        return ret_str

    def sell_goods(self, good, broker_roll):
        good_sell_dm = self.sell_goods_dm[good]
        true_roll = broker_roll + good_sell_dm
        true_roll = max(true_roll, -1)
        true_roll = min(true_roll, 21)
        true_roll += 1
        price_change = self.modified_price_table_plus_one[true_roll][1]

        new_price = price_change * self.trade_goods_pri[good]

        ret_str = "At a " + str(int(price_change * 100)) + "% you can sell " + \
                  good + " at " + str(int(new_price)) + " per ton"

        return ret_str

    def size_to_time(self, size):
        for i in range(11):
            distance, time = self.distance_to_time_map[i]
            if size <= distance:
                return time

    def atmos_desc(self, atmos_list):
        ret_map = {}
        for desc in atmos_list:
            if desc in self.atmosphere_description_map.keys():
                ret_map[desc] = self.atmosphere_description_map[desc]
            else:
                ret_map[desc] = "No description"

        return ret_map

    @staticmethod
    def set_to_rep(char_set):
        return str(char_set[0]) + " -> " + str(char_set[1])

    @staticmethod
    def pass_rolling(pass_pos_list):
        total = 0
        for i in range(pass_pos_list[0]):
            total += random.randint(1, 6)

        for i in range(pass_pos_list[1]):
            total -= random.randint(1, 6)

        total -= pass_pos_list[2]

        ret = max(total, 0)
        return ret

    @staticmethod
    def freight_rolling(freight_pos_list):
        total = 0
        for i in range(freight_pos_list[0]):
            total += random.randint(1, 6)

        total += freight_pos_list[1]

        ret = max(total, 0)
        return ret

    @staticmethod
    def lot_to_cargo(amount, mod, cargo_map):
        for i in range(amount):
            single_cargo = random.randint(1, 6) * mod
            if single_cargo in cargo_map.keys():
                cargo_map[single_cargo] += 1
            else:
                cargo_map[single_cargo] = 1

    @staticmethod
    def table_to_row(columns, data_map):
        ret_dict = {}
        for i in range(len(columns)):
            ret_dict[columns[i]] = data_map[i]

        return ret_dict

    def __str__(self):
        total_str = ""

        total_str += "NAME: " + self.name + "\n"
        total_str += "LOCATION: " + self.location + "\n"
        total_str += "STARPORT QUALITY: " + self.set_to_rep(self.starport_quality) + \
                     " -> " + \
                     str(self.table_to_row(self.starport_info_columns,
                                           self.starport_info_map[self.characteristics[0]])) + "\n"
        total_str += "SIZE (DIAMETER): " + self.set_to_rep(self.size) + " km" +  " -> " + \
                     str(self.size_to_time(self.size[1]) / 3600) + " hours or " + \
                     str(self.size_to_time(self.size[1]) / (24 * 3600)) + " days" + "\n"
        total_str += "ATMOSPHERE TYPE: " + self.set_to_rep(self.atmosphere_type) + \
                     " -> " + str(self.atmos_desc(self.atmosphere_type[1])) + "\n"
        total_str += "HYDROGRAPHIC PERCENTAGE: " + self.set_to_rep(self.hydrographic_percentage) + "\n"
        total_str += "POPULATION: " + self.set_to_rep(self.population) + "\n"
        total_str += "GOVERNMENT TYPE: " + self.set_to_rep(self.government_type) + "\n"
        total_str += "LAW LEVEL: " + str(self.law_level) + \
                     " -> " + \
                     str(self.table_to_row(self.law_level_columns, self.law_level_table[min(9, self.law_level)])) + "\n"
        total_str += "TECH LEVEL: " + str(self.tech_level) + "\n"
        total_str += "BASES: " + str(self.bases) + "\n"
        total_str += "TRADE CODES: " + str(self.trade_codes) + "\n"
        total_str += "FACTION: " + str(self.faction) + "\n"
        total_str += "DEFAULT TRADE GOODS: " + str(self.default_trade_goods_dm_map) + "\n"
        total_str += "SELL GOODS DM: " + str(self.sell_goods_dm) + "\n"

        return total_str
