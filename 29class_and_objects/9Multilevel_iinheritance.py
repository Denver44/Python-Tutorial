# -------------------------------------------------------- MUTLILEVEL INHERITANCES --------------------------------------------------------//
class Dad:
    basketball = 1


class Son(Dad):
    Dance = 1
    basketball = 88

    def printdance(self):
        print(f"Son know {self.Dance} of dance form")


class Grandson(Son):
    Dance = 6
    basketball = 55

    def printmy(self):
        print(
            f"I am Mordern era Grandson so i know {self.Dance} types of dances and my basketball skill is {self.basketball}")


Danny = Dad()
larry = Son()
larry.printdance()
ali = Grandson()
ali.printdance()

kerry = Grandson()
kerry.printmy()
