

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


if __name__ == "__main__":
    # Prints out the dict key types for DemoParser
    from awpy.parser import DemoParser

    demo_parser = DemoParser(
        demofile="tests/test_demo_file.dem",
        outpath=None,
        demo_id="test_demo",
        parse_frames=True,
        log=False,
        parse_rate=128,
        parse_kill_frames=False,
        trade_time=5,
        dmg_rolled=False,
        buy_style="hltv",
        json_indentation=True
    )

    json_data = demo_parser.parse(return_type="json", clean=True)
    recursive_key_print(data=json_data, space="")
