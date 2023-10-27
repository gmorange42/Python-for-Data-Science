def NULL_not_found(object: any) -> int:
    if type(object) == type(None):
        print("Nothing:", object , type(object))
        return 0
    elif type(object) == type(float() and object == 'NaN'):
        print("Cheese:", object , type(object))
        return 0
    elif type(object) == type(int()) and object == 0:
        print("Zero:", object , type(object))
        return 0
    elif type(object) == type(str()) and len(object) == 0:
        print("Empty:", type(object))
        return 0
    elif type(object) == type(bool()) and object == False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Type not Found")
    return 1
