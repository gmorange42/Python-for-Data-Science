from abc import ABC, abstractmethod


class Character(ABC):
    '''An abstract class to represent a Character.

    Attributes:
    first_name (str): the first name of the character.
    is_alive (bool): the state of life of the character.

    Methods:
    __init__(self, first_name, is_alive=True): set attributes.
    die(): set the attribute is_alive to False.
    '''

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Init an abstract method

        Parameters:
        argument 1 (str): set the attribute first_name.
        argument 2(bool=True: set the attribute is_alive.
        '''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Pass the attribute is_Alive to False'''
        self.is_alive = False


class Stark(Character):
    '''Stark class is inherited from Character class

    Attributes:
    first_name (str): the first name of the character.
    is_alive (bool): the state of life of the character.

    Methods:
    __init__(self, first_name, is_alive=True): set attributes.
    die(): set the attribute is_alive to False.
    '''

    def __init__(self, first_name, is_alive=True):
        '''Set the attributes, inherited from Character class

        Parameters:
        argument 1 (str): set the attribute first_name.
        argument 2(bool=True): set the attribute is_alive.
        '''
        Character.__init__(self, first_name, is_alive)


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == '__main__':
    main()
