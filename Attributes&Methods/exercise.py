class PreciousStone:
    numberOfPreciousStone = 0
    listOfPreciousStone = []

    def __init__(self,name):
        self.name = name
        PreciousStone.numberOfPreciousStone+=1

        if PreciousStone.numberOfPreciousStone <= 5:
            PreciousStone.listOfPreciousStone.append(self)
        else:
            del PreciousStone.listOfPreciousStone[0]
            PreciousStone.listOfPreciousStone.append(self)
    @staticmethod
    def display_precious_stones():
        for preciousStone in PreciousStone.listOfPreciousStone:
            print(preciousStone.name,end='\n')


preciousStoneOne  = PreciousStone("Ruby")
preciousStoneTwo  = PreciousStone("Emerald")
preciousStoneThree  = PreciousStone("Sapphire")
preciousStoneFour  = PreciousStone("Diamond")
preciousStoneFive  = PreciousStone("Amber")

preciousStoneFive.display_precious_stones()

print('----------------------\n')
preciousStoneSix = PreciousStone("another precious Stone")

preciousStoneSix.display_precious_stones()
#t
