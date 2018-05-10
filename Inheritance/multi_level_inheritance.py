class MusicalInstruments:
    number_of_major_keys = 12

class StringInstruments(MusicalInstruments):
    type_of_wood = 'Tonewood'

class Guitar(StringInstruments):
    def __init__(self,name):
        self.number_of_strings = 6
        self.name = name
        print('''The guitar {} consists of {} strings.It is made of {} and it can play {} keys'''
        .format(self.name,self.number_of_strings,self.type_of_wood,self.number_of_major_keys))

gibson = Guitar('Gibson')
les_paul = Guitar('Les Paul')
sg = Guitar('Sg')
