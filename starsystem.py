def copy_to_args(total_str, has_bases, has_trade, has_faction):


class StarSystem:

    base_map = {'N': "Naval Base", "S": "Scout Base", "R": "Research Base", "T": "TAS Hostel",
                "C": "Imperial Consulate", "P": "Pirate Base", "G": "Gas Giant"}

    trade_codes = {"Ag": "Agricultural", "As": "Asteroid", "Ba": "Barren", "De": "Desert", "Fl": "Fluid Oceans",
                   "Ga": "Garden", "Hi": "High Population", "Ht": "High Technology", "Ic": "Ice-Capped",
                   "In": "Industrial", "Lo": "Low Population", "Lt": "Low Technology", "Na": "Non-Agricultural",
                   "Ni": "Non-Industrial", "Po": "Poor", "Ri": "Rich", "Va": "Vacuum", "Wa": "Water World",
                   "A": "Amber Zone", "R": "Red Zone"}

    starport_quality = {'A': "Excellent", 'B': "Good", 'C': "Routine", 'D': "Poor", 'E': "Frontier", 'X': "No Starport"}

    size_table = ["800 km", "1,600 km", "3,200 km", "4,800 km", "6,400 km", "8,000 km", "9,600 km", "11,200 km",
                  "12,800 km", "14,400 km", "16,000 km"]

    atmosphere_table = ["None", "Trace", "Very Thin, Tainted", "Very Thin", "Thin, Tainted", "Thin", "Standard",
                        "Standard, Tainted", "Dense", "Dense, Tainted", "Exotic", "Corrosive", "Insidious",
                        "Dense, High", "Thin, Low", "Unusual"]

    hydrographic_percentage_table = ["0%–5%", "6%–15%", "16%–25%", "26%–35%", "36%–45%", "46%–55%", "56%–65%", "66%–75%",
                               "76%–85%", "86%–95%", "96–100%"]

    population_table = ["None", "Few", "Hundreds", "Thousands", "Tens of thousands", "Hundreds of thousands",
                        "Millions", "Tens of millions", "Hundreds of millions", "Billions", "Tens of billions",
                        "Hundreds of billions", "Trillions"]

    government_table = ["None", "Company/corporation", "Participating democracy", "Self-perpetuating oligarchy",
                        "Representative democracy", "Feudal technocracy", "Captive government", "Balkanisation",
                        "Civil service bureaucracy", "Impersonal Bureaucracy", "Charismatic dictator",
                        "Non-charismatic leader", "Charismatic oligarchy", "Religious dictatorship"]


    def __init__(self, name, location, characteristics, bases, trade_codes, faction):
        self.name = name
        self.location = location
        self.characteristics = characteristics
        self.starport_quality = self.starport_quality[characteristics[0]]
        self.size = self.hex_char_to_istic(1, self.size_table)
        self.atmosphere_type = self.hex_char_to_istic(2, self.atmosphere_table)
        self.hydrographic_percentage = self.hex_char_to_istic(3, self.hydrographic_percentage_table)
        self.population = self.hex_char_to_istic(4, self.population_table)
        self.government_type = self.hex_char_to_istic(5, self.government_table)
        self.law_level = str(self.hex_char_to_int(6))
        self.tech_level = str(self.hex_char_to_int(8))

    def hex_char_to_int(self, index):
        return int(((self.characteristics)[index]), 16)

    def hex_char_to_istic(self, index, istic_list):
        return istic_list[self.hex_char_to_int(index)]