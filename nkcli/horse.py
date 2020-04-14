class Horse(object):
    netkeiba_id = 0
    name = "name"
    sex = "stalion_or_mare"
    foaled = "YYYY"
    color = ""
    record = ""
    earnings = ""
    retired = True

    def __init__(self, id_):
        self.netkeiba_id = id_

    def print(self):
        print("ID:       ", self.netkeiba_id)
        print("Name:     ", self.name)
        print("Retired:  ", self.retired)
        print("Sex:      ", self.sex)
        print("Foaled:   ", self.foaled)
        print("Color:    ", self.color)
        print("Record:   ", self.record)
        print("Earnings: ", self.earnings)


class Pedigree(object):

    def __init__(self, sire, dam):
        self.sire = sire
        self.dam = dam

    def print(self):
        if self.sire["international_name"] != "":
            print("Sire: {} {} ({})".format(self.sire["id"], self.sire["name"], self.sire["international_name"]))
        else:
            print("Sire: {} {}".format(self.sire["id"], self.sire["name"]))

        if self.dam["international_name"] != "":
            print("Dam:  {} {} ({})".format(self.dam["id"], self.dam["name"], self.dam["international_name"]))
        else:
            print("Dam:  {} {}".format(self.dam["id"], self.dam["name"]))
