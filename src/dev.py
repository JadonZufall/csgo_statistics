# This file is used for testing awpy features, should be removed from any compiled builds of the program.
from awpy.parser import DemoParser


demo_parser = DemoParser(
    demofile="test_demo_file.dem",
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



