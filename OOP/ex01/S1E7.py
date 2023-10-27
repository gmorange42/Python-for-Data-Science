from S1E9 import Character


class Baratheon(Character):
    '''Baratheon class is inherited from Character class

    Attributes:
    first_name (str): the first name of the character.
    eyes (str): the eyes color.
    hairs (str): the hairs color.
    is_alive (bool): the state of life of the character.

    Methods:
    __init__(self, first_name, is_alive=True): set attributes.
    die(): set the attribute is_alive to False.
    '''

    def __init__(self, first_name, is_alive=True, eyes="brown", hairs="dark"):
        '''Set the attributes, first_name and is_alive inherited
        from Character class

        Parameters:
        argument 1 (str): set the attribute first_name.
        argument 2 (bool=True): set the attribute is_alive.
        argument 3 (str="borwn"): set the attribute eyes.
        argument 4 (str="dark"): set the attribute hairs.
        '''
        Character.__init__(self, first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        '''Return a string with the attributes first_name, eyes and hairs '''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        '''Return a string with the attributes first_name, eyes and hairs '''
        return self.__str__()


class Lannister(Character):
    '''Lannister class is inherited from Character class

    Attributes:
    first_name (str): the first name of the character.
    eyes (str): the eyes color.
    hairs (str): the hairs color.
    is_alive (bool): the state of life of the character.

    Methods:
    __init__(self, first_name, is_alive=True): set attributes.
    die(): set the attribute is_alive to False.
    create_lannister(cls, first_name, is_alive=True).
    '''

    def __init__(self, first_name, is_alive=True, eyes="blue", hairs="light"):
        '''Set the attributes, first_name and is_alive inherited
        from Character class

        Parameters:
        argument 1 (str): set the attribute first_name.
        argument 2 (bool=True): set the attribute is_alive.
        argument 3 (str="blue"): set the attribute eyes.
        argument 4 (str="light"): set the attribute hairs.
        '''
        Character.__init__(self, first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        '''Return a string with the attributes first_name, eyes and hairs '''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        '''Return a string with the attributes first_name, eyes and hairs '''
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True,
                         eyes="blue", hairs="light"):
        '''Create a new instance of Lannister with the parameters

        Parameters:
        argument 1 (str): set the attribute first_name.
        argument 2 (bool=True): set the attribute is_alive.
        argument 3 (str="blue"): set the attribute eyes.
        argument 4 (str="light"): set the attribute hairs.

        Return a new instance of Lannister
        '''
        return cls(first_name, is_alive, eyes, hairs)


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
Alive : {Jaine.is_alive}")


if __name__ == '__main__':
    main()
