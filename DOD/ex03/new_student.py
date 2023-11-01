import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generates a random id and returns it'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Class to create student objects

    Attributes:
    name (str): the student's name.
    surname (str): the student's surname.
    active (bool): the student's activity status (True by default).
    login (str): the student's login (unparameterizable).
    id (str): the student's login (random, unparameterizable).

    Method:
    __post_init__(self)
    '''

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        '''Sets the student's id with generate_id()'''
        self.login = f'{self.name[0].capitalize()}{self.surname.lower()}'
        self.id = generate_id()


def main():
    '''Tests the Student class'''
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == '__main__':
    main()
