class SubSector:

    def  __init__(self, number):
        self.number = number
        self.starsystems = {}

    def add_starsystem(self, starsystem):
        self.starsystems[starsystem.location] = starsystem

    def get_starsystem(self, starsystem_location):
        return self.starsystems[starsystem_location]