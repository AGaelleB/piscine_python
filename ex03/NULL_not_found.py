def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing: None <class 'NoneType'>")
    elif  object != object:
        print("Cheese: nan <class 'float'>")
    elif object == 0 and type(object) is int:
        print("Zero: 0 <class 'int'>")
    elif  object == '':
        print("Empty: <class 'str'>")
    elif object == False and type(object) is bool:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not Found")
        return 1
    return 0