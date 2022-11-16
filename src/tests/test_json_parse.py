from unittest import TestCase

from awpy.parser import DemoParser

from src.replay_data import ReplayData


class TestJsonParse(TestCase):
    def setUp(self) -> None:
        demo_parser = DemoParser(demofile="test_demo_file.dem", outpath=None, demo_id="test_demo", parse_frames=True,
                                 log=False, parse_rate=128, parse_kill_frames=False, trade_time=5, dmg_rolled=False,
                                 buy_style="hltv", json_indentation=True)
        self.json_data = demo_parser.parse(return_type="json", clean=True)

    def test_object_stack(self) -> None:
        replay_data = ReplayData(json_data=self.json_data, load_player_data=True, load_round_data=True)
        self.assertIsNotNone(replay_data)


