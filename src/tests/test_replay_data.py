from unittest import TestCase

from awpy.parser import DemoParser

from src.replay_data import ReplayData


class TestReplayData(TestCase):
    def setUp(self) -> None:
        demo_parser = DemoParser(demofile="test_demo_file.dem", outpath=None, demo_id="test_demo", parse_frames=True,
                                 log=False, parse_rate=128, parse_kill_frames=False, trade_time=5, dmg_rolled=False,
                                 buy_style="hltv", json_indentation=True)

        self.json_data = demo_parser.parse(return_type="json", clean=True)

    def test_replay_parsing(self) -> None:
        replay_data = ReplayData(json_data=self.json_data, load_player_data=False, load_round_data=False)
        self.assertIsNotNone(replay_data)

    def test_round_parsing(self) -> None:
        replay_data = ReplayData(json_data=self.json_data, load_player_data=False, load_round_data=False)
        self.assertNotEqual(replay_data.number_of_rounds, 0)
        for i in range(0, replay_data.number_of_rounds):
            self.assertIsNotNone(replay_data.get_round_data(round_number=i))

    def test_player_parsing(self) -> None:
        replay_data = ReplayData(json_data=self.json_data, load_player_data=True, load_round_data=False)
        self.assertNotEqual(replay_data.number_of_players, 0)
        for i in range(0, replay_data.number_of_players):
            self.assertIsNotNone(replay_data.get_player_by_index(index=i))
