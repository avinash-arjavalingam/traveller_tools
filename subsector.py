from starsystem import StarSystem


class SubSector:

    def __init__(self):
        self.this_planet = None
        self.starsystems = {}
        self.is_first_time = True
        self.add_starsystem(("Twovapu", "0102", "D664210-4", "SG", "Ga Lo Lt A"))
        print(self.get_starsystem("0102"))
        self.add_starsystem(("Qutra", "0104", "D446545-5", "SG", "Ag Lt Ni"))
        print(self.get_starsystem("0104"))
        self.add_starsystem(("Qewra", "0105", "D46668A-3", "SG", "Ag Lt Ni Ri A"))
        print(self.get_starsystem("0105"))
        self.add_starsystem(("Twotra","0106", "D510211-8", "G", "Lo"))
        print(self.get_starsystem("0106"))
        self.add_starsystem(("Vavaqe", "0108", "C583897-3", "SRG", "Lt Ri"))
        print(self.get_starsystem("0108"))
        self.add_starsystem(("Tretwo", "0109", "B436000-0", "NTCG", "Ba"))
        print(self.get_starsystem("0109"))
        self.add_starsystem(("Yid", "0110", "B879354-10", "T", "Lo"))
        print(self.get_starsystem("0110"))
        self.add_starsystem(("Yiphunge", "0202", "D240731-4", "S", "De Lt Po"))
        print(self.get_starsystem("0202"))
        self.add_starsystem(("Wraye", "0206", "C468AC9-9", "SG", "Hi A"))
        print(self.get_starsystem("0206"))
        self.add_starsystem(("Yequtra", "0208", "D570830-3", "G", "De Lt A"))
        print(self.get_starsystem("0208"))
        self.add_starsystem(("Puye", "0209", "C7A0000-0", "P", "Ba De A"))
        print(self.get_starsystem("0209"))
        self.add_starsystem(("Xeguwho", "0301", "E120511-11", "G", "De Ni Po", "[Scusci]"))
        print(self.get_starsystem("0301"))
        self.add_starsystem(("Yisci", "0302", "C53368A-9", "G", "Na Ni Po A", "[Scusci]"))
        print(self.get_starsystem("0302"))
        self.add_starsystem(("Qafla", "0304", "D585202-8", "SG", "Ga Lo A", "[Drafla]"))
        print(self.get_starsystem("0304"))
        self.add_starsystem(("Yevapu", "0307", "D260110-8", "G", "De Lo A"))
        print(self.get_starsystem("0307"))
        self.add_starsystem(("Pupu", "0308", "C692257-7", "S", "Lo"))
        print(self.get_starsystem("0308"))
        self.add_starsystem(("Phutre", "0309", "D536267-5", "SG", "Lo Lt"))
        print(self.get_starsystem("0309"))
        self.add_starsystem(("Shaqa", "0403", "C100366-9", "SG", "Lo Va", "[Drafla]"))
        print(self.get_starsystem("0403"))
        self.add_starsystem(("Fudra", "0404", "C483986-8", "PG", "Hi", "[Drafla]"))
        print(self.get_starsystem("0404"))
        self.add_starsystem(("Pudva", "0406", "C636652-8", "G", "Ni"))
        print(self.get_starsystem("0406"))
        self.add_starsystem(("Zudqe", "0408", "A200657-14", "NTC", "Ht Na Ni Va"))
        print(self.get_starsystem("0408"))
        self.add_starsystem(("Yeje", "0409", "D410000-0", "SG", "Ba"))
        print(self.get_starsystem("0409"))
        self.add_starsystem(("Rosci", "0501", "B68278B-10", "NTCG", "Ri A", "[Scusci]"))
        print(self.get_starsystem("0501"))
        self.add_starsystem(("Sciyicho", "0503", "A255255-12", "STG", "Ht Lo", "[Scusci]"))
        print(self.get_starsystem("0503"))
        self.add_starsystem(("Scicho", "0504", "D742422-5", "SPG", "Lt Ni Po", "[Scusci]"))
        print(self.get_starsystem("0504"))
        self.add_starsystem(("Yipuwra", "0510", "BAD7668-11", "TCG", "Fl Ni A"))
        print(self.get_starsystem("0510"))
        self.add_starsystem(("Yiscu", "0601", "E200477-8", "G", "Ni Va A", "[Scusci]"))
        print(self.get_starsystem("0601"))
        self.add_starsystem(("Sciro", "0602", "D232533-7", "SG", "Ni Po", "[Scusci]"))
        print(self.get_starsystem("0602"))
        self.add_starsystem(("Jifo", "0604", "D445130-6", "G", "Lo A", "[Scusci]"))
        print(self.get_starsystem("0604"))
        self.add_starsystem(("Lozhgha", "0605", "D200000-0", "G", "Ba Va", "[Zhipri]"))
        print(self.get_starsystem("0605"))
        self.add_starsystem(("Flixewho", "0702", "C769667-8", "G", "Ni Ri", "[Scusci]"))
        print(self.get_starsystem("0702"))
        self.add_starsystem(("Raro", "0705", "B325343-12", "TCG", "Ht Lo", "[Zhipri]"))
        print(self.get_starsystem("0705"))
        self.add_starsystem(("Pritru", "0706", "C337227-9", "SPG", "Lo", "[Zhipri]"))
        print(self.get_starsystem("0706"))
        self.add_starsystem(("Vaje", "0708", "A9DA651-12", "NTC", "Fl Ht Ni Wa A"))
        print(self.get_starsystem("0708"))
        self.add_starsystem(("Zuye", "0709", "A110864-14", "CG", "Ht Na"))
        print(self.get_starsystem("0709"))
        self.add_starsystem(("Thufli", "0801", "A99A330-10", "NT", "Lo Wa A", "[Scusci]"))
        print(self.get_starsystem("0801"))
        self.add_starsystem(("Gugurho", "0802", "E977569-7", "G", "Ag Ga Ni A", "[Scusci]"))
        print(self.get_starsystem("0802"))
        self.add_starsystem(("Yospepri", "0805", "C030457-9", "RC", "De Ni Po", "[Zhipri]"))
        print(self.get_starsystem("0805"))
        self.add_starsystem(("Traphu", "0806", "A565595-9", "NRG", "Ag Ga Ni"))
        print(self.get_starsystem("0806"))

    def add_starsystem(self, starsystem_args):
        self.starsystems[starsystem_args[1]] = StarSystem(*starsystem_args)

    def get_starsystem(self, starsystem_location):
        return self.starsystems[starsystem_location]

    def start_game(self, starting_planet_sector):
        self.this_planet = self.get_starsystem(starting_planet_sector)
        if self.is_first_time:
            self.this_planet.clear_session()
            self.this_planet.get_session_purchase_goods()
            print("PLANET YOU ARE IN")
            print("--------------------------------------------------------------------------------------------------")
            print("")
            print(self.get_starsystem(self.this_planet.location))
            print("")
            print("--------------------------------------------------------------------------------------------------")
            self.is_first_time = False
        print("")
        print("ACTIONS:")
        print("[Move]    [Passengers]    [Freight]    [Mail]    [Buy]    [Sell]")
        decision = input("What would you like to do? ").lower().strip()
        if decision == "move":
            self.move()
        elif decision == "passengers":
            self.passengers()
        elif decision == "freight":
            self.freight()
        elif decision == "mail":
            self.mail()
        elif decision == "buy":
            self.buy()
        elif decision == "sell":
            self.sell()
        else:
            print("Invalid action!")

    def move(self):
        other_planet = input("What starsytem location you like to go? ").strip()
        if other_planet not in self.starsystems.keys():
            print("Not a valid starsystem 4 digit location!")
        else:
            self.this_planet.clear_session()
            self.this_planet = self.starsystems[other_planet]
            self.is_first_time = True

    def passengers(self):
        other_planet = input("What other planet (location) are you considering? ").strip()
        if other_planet not in self.starsystems.keys():
            print("Not a valid starsystem 4 digit location!")
        else:
            other_planet_obj = self.get_starsystem(other_planet)
            print("")
            print("PLANET CHOSEN: ")
            print(other_planet_obj)
            print("")
            print("PASSENGER ACTIONS:")
            print("1: [Get passengers DM]    2: [See available passengers]")
            two_branch = input("What passenger action would you like to do? Enter the corresponding number: ").strip()
            if two_branch == "1":
                print(self.this_planet.get_passengers_base_dm(other_planet_obj))
            elif two_branch == "2":
                pass_check = int(
                    input("Enter the carouse check to get more passengers (Enter 8 for no check): ").strip())
                print(self.this_planet.get_passengers(other_planet_obj, pass_check))

            else:
                print("Invalid action!")

    def freight(self):
        other_planet = input("What other planet (location) are you considering? ").strip()
        if other_planet not in self.starsystems.keys():
            print("Not a valid starsystem 4 digit location!")
        else:
            other_planet_obj = self.get_starsystem(other_planet)
            print("")
            print("PLANET CHOSEN: ")
            print(other_planet_obj)
            print("")
            print("FREIGHT ACTIONS:")
            print("1: [Get freight DM]    2: [See available freight]")
            two_branch = input("What freight action would you like to do? Enter the corresponding number: ").strip()
            if two_branch == "1":
                print(self.this_planet.get_freight_base_dm(other_planet_obj))
            elif two_branch == "2":
                print(self.this_planet.get_freight(other_planet_obj))

            else:
                print("Invalid action!")

    def mail(self):
        other_planet = input("What other planet (location) are you considering? ").strip()
        if other_planet not in self.starsystems.keys():
            print("Not a valid starsystem 4 digit location!")
        else:
            other_planet_obj = self.get_starsystem(other_planet)
            print("")
            print("PLANET CHOSEN: ")
            print(other_planet_obj)
            print("")
            has_guns_str = input("Does the ship have guns? y/n: ").lower().strip()
            has_guns = None
            if has_guns_str == "y" or has_guns_str == "yes":
                has_guns = True
            elif has_guns_str == "n" or has_guns_str == "no":
                has_guns = False
            else:
                print("Invalid action!")
                return
            navy_scout_rank = int(input("What is the highest naval/scout rank achieved (0 for none): ").strip())
            soc_scout_dm = int(input("What is the highest Social Standing modifier? ").strip())
            print("MAIL ACTIONS:")
            print("1: [Get mail DM]    2: [See if mail is available]")
            two_branch = input("What mail action would you like to do? Enter the corresponding number: ").strip()
            if two_branch == "1":
                print(self.this_planet.get_mail_dm(other_planet_obj, has_guns, navy_scout_rank, soc_scout_dm))
            elif two_branch == "2":
                mail_check = int(input("Enter the 2d6 check to see if there is mail: ").strip())
                print(self.this_planet.has_mail(other_planet_obj, has_guns, navy_scout_rank, soc_scout_dm, mail_check))

            else:
                print("Invalid action!")

    def buy(self):
        sesh_goods = self.this_planet.get_session_purchase_goods()
        print("BUY ACTIONS:")
        print("1: [See available goods]    2: [Buy goods]")
        two_branch = input("What buy action would you like to do? Enter the corresponding number: ").strip()
        if two_branch == "1":
            print(sesh_goods)
        elif two_branch == "2":
            good = input("What good would you like to buy (Capitalization matters)? ").strip()
            if good not in sesh_goods.keys():
                print("Invalid good!")
            else:
                broker_check = int(input("Enter the broker check to see how good of a price you get: ").strip())
                print(self.this_planet.buy_goods(good, broker_check))
        else:
            print("Invalid action!")

    def sell(self):
        good = input("What good would you like to sell (Capitalization matters)? ").strip()
        if good not in self.this_planet.sell_goods_dm.keys():
            print("Invalid good!")
        else:
            broker_check = int(input("Enter the broker check to see how good of a price you get: ").strip())
            print(self.this_planet.sell_goods(good, broker_check))

