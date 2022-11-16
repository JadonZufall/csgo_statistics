from awpy.parser import DemoParser
from src.utils.dict_type_print import print_dict_types


if __name__ == "__main__":
    # Prints out the dict key types for DemoParser
    demo_parser = DemoParser(
        demofile="tests/test_demo_file.dem",
        outpath=None,
        demo_id="test_demo",
        parse_frames=True,
        log=False,
        parse_rate=10_000,
        parse_kill_frames=False,
        trade_time=5,
        dmg_rolled=False,
        buy_style="hltv",
        json_indentation=True
    )

    json_data = demo_parser.parse(return_type="json", clean=True)
    print_dict_types(data=json_data)
