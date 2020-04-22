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
                             "Barren": [-5, -5, float('-inf'), -5], "Desert": [-1, -1, -3, 0],
                             "Fluid Oceans": [0, 0, -3, 0], "Garden": [2, 2, 2, 1], "High Population": [0, 4, 2, -1],
                             "Ice-Capped": [1, -1, -3, 0], "Industrial": [2, 1, 3, 2], "Low Population": [0, -4, -5, 0],
                             "Non-Agricultural": [0, 0, -3, 1], "Non-Industrial": [0, -1, -3, 1],
                             "Poor": [-2, -1, -3, -3], "Rich": [-1, 2, 2, 2], "Water World": [0, 0, -3, 0],
                             "Amber Zone": [2, -2, 5, -5], "Red Zone": [4, -4, -5, float('-inf')]}

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

    starport_quality_map = {'A': "Excellent", 'B': "Good", 'C': "Routine", 'D': "Poor", 'E': "Frontier",
                            'X': "No Starport"}

    size_table = ["800 km", "1,600 km", "3,200 km", "4,800 km", "6,400 km", "8,000 km", "9,600 km", "11,200 km",
                  "12,800 km", "14,400 km", "16,000 km"]

    atmosphere_table = ["None", "Trace", "Very Thin, Tainted", "Very Thin", "Thin, Tainted", "Thin", "Standard",
                        "Standard, Tainted", "Dense", "Dense, Tainted", "Exotic", "Corrosive", "Insidious",
                        "Dense, High", "Thin, Low", "Unusual"]

    hydrographic_percentage_table = ["0%–5%", "6%–15%", "16%–25%", "26%–35%", "36%–45%", "46%–55%", "56%–65%",
                                     "66%–75%", "76%–85%", "86%–95%", "96–100%"]

    population_table = ["None", "Few", "Hundreds", "Thousands", "Tens of thousands", "Hundreds of thousands",
                        "Millions", "Tens of millions", "Hundreds of millions", "Billions", "Tens of billions",
                        "Hundreds of billions", "Trillions"]

    government_table = ["None", "Company/corporation", "Participating democracy", "Self-perpetuating oligarchy",
                        "Representative democracy", "Feudal technocracy", "Captive government", "Balkanisation",
                        "Civil service bureaucracy", "Impersonal Bureaucracy", "Charismatic dictator",
                        "Non-charismatic leader", "Charismatic oligarchy", "Religious dictatorship"]

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
        self.tech_level = self.hex_char_to_int(8)

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
        for code in self.trade_codes:
            if code in self.trade_goods_default_available.keys():
                self.default_trade_goods = self.default_trade_goods.union(self.trade_goods_default_available[code])

    def hex_char_to_int(self, index):
        return int((self.characteristics[index]), 16)

    def hex_char_to_istic(self, index, istic_list):
        return istic_list[self.hex_char_to_int(index)]

    @staticmethod
    def set_to_rep(char_set):
        return str(char_set[0]) + " -> " + str(char_set[1])

    def __str__(self):
        total_str = ""

        total_str += "NAME: " + self.name + "\n"
        total_str += "LOCATION: " + self.location + "\n"
        total_str += "STARPORT QUALITY: " + self.set_to_rep(self.starport_quality) + "\n"
        total_str += "SIZE (DIAMETER): " + self.set_to_rep(self.size) + "\n"
        total_str += "ATMOSPHERE TYPE: " + self.set_to_rep(self.atmosphere_type) + "\n"
        total_str += "HYDROGRAPHIC PERCENTAGE: " + self.set_to_rep(self.hydrographic_percentage) + "\n"
        total_str += "POPULATION: " + self.set_to_rep(self.population) + "\n"
        total_str += "GOVERNMENT TYPE: " + self.set_to_rep(self.government_type) + "\n"
        total_str += "LAW LEVEL: " + str(self.law_level) + "\n"
        total_str += "TECH LEVEL: " + str(self.tech_level) + "\n"
        total_str += "BASES: " + str(self.bases) + "\n"
        total_str += "TRADE CODES: " + str(self.trade_codes) + "\n"
        total_str += "FACTION: " + str(self.faction) + "\n"
        total_str += "DEFAULT TRADE GOODS: " + str(self.default_trade_goods) + "\n"

        return total_str