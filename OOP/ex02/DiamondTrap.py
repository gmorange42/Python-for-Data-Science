from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King class is inherited from Baratheon and Lannister classes

    Attributes:
    first_name (str): the first name of the character.
    eyes (str): the eyes color, brown.
    hairs (str): the hairs color, dark.
    is_alive (bool): the state of life of the character.

    Methods:
    __init__(self, first_name, is_alive=True): set attributes.
    die(): pass the attribute is_alive to False.
    set_eyes(self, color): set the attribute eyes.
    set_hairs(self, color): set the attribute hairs.
    get_eyes(self): return the eyes color.
    get_hairs(self): return the hairs color.

    '''

    def __init__(self, first_name, is_alive=True):
        '''Set the attributes, first_name and is_alive inherited
        from Character class

        Parameters:
        argument 1 (str): set the attribute first_name.
        argument 2 (bool=True): set the attribute is_alive.
        '''
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        '''Set the attribute eyes'''
        self.eyes = color

    def set_hairs(self, color):
        '''Set the attribute hairs'''
        self.hairs = color

    def get_eyes(self):
        '''return the eyes color'''
        return self.eyes

    def get_hairs(self):
        '''return the hairs color'''
        return self.hairs

    @property
    def prop_eyes(self):
        return (self.eyes)

    @prop_eyes.setter
    def prop_eyes(self, color):
        self.eyes = color

    @property
    def prop_hairs(self):
        return (self.hairs)

    @prop_hairs.setter
    def prop_hairs(self, color):
        self.hairs = color

    _eyes = property(get_eyes, set_eyes)
    _hairs = property(get_hairs, set_hairs)


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

    Joffrey.prop_eyes = "gray"
    print(Joffrey.prop_eyes)
    Joffrey.prop_hairs = "Red"
    print(Joffrey.prop_hairs)

    Joffrey._eyes = "green"
    print(Joffrey._eyes)
    Joffrey._hairs = "bald"
    print(Joffrey._hairs)
    print(Joffrey.__dict__)


if __name__ == '__main__':
    main()
