def all_thing_is_obj(object: any) -> int:
    if type(object) == type(list()):
        print("List :" , type(object))
    elif type(object) == type(tuple()):
        print("Tuple :" , type(object))
    elif type(object) == type(set()):
        print("Set :" , type(object))
    elif type(object) == type(dict()):
        print("Dict :" , type(object))
    elif type(object) == type(str()):
        print("Brian is in the kitchen :" , type(object))
    else:
        print("Type not found")
    return 42
