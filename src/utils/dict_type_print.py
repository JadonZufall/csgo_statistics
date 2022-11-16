def recursive_key_print(data: dict, space="") -> None:
    for i in data.keys():
        print(space + i + ": " + str(type(data[i])))
        if isinstance(data[i], dict):
            print(space + "{")
            recursive_key_print(data=data[i], space=space + "  ")
            print(space + "}")
        elif isinstance(data[i], list):
            if len(data[i]) == 0:
                print(space + "[")
                print(space + "  " + "NoneType")
                print(space + "]")
            elif isinstance(data[i][0], dict):
                print(space + "[")
                print(space + "  " + "{")
                recursive_key_print(data=data[i][0], space=space + "    ")
                print(space + "  " + "}")
                print(space + "]")
            else:
                print(space + "[")
                print(space + "  " + str(type(data[i][0])))
                print(space + "]")


def print_dict_types(data: dict) -> None:
    """ Function for printing a dictionary keys and all of its nested types. """
    recursive_key_print(data=data, space="")