from unittest import TestCase

from src.player_data import PlayerData


class TestPlayerData(TestCase):
    def setUp(self) -> None:
        self.example_json = {
            'steamID': 76561197999186947, 'playerName': 'fer', 'teamName': 'Team Brazil', 'isBot': False,
            'totalRounds': 24, 'kills': 22, 'deaths': 16, 'kdr': 1.38, 'assists': 0, 'tradeKills': 2, 'teamKills': 0,
            'suicides': 0, 'flashAssists': 0, 'totalDamageGiven': 2172, 'totalDamageTaken': 1896,
            'totalTeamDamageGiven': 27, 'adr': 90.5, 'totalShots': 339, 'shotsHit': 62, 'accuracy': 0.18,
            'rating': 1.21, 'kast': 58.3, 'hs': 12, 'hsPercent': 0.55, 'firstKills': 5, 'firstDeaths': 4,
            'utilityDamage': 209, 'smokesThrown': 9, 'flashesThrown': 12, 'heThrown': 8, 'fireThrown': 12,
            'enemiesFlashed': 13, 'teammatesFlashed': 6, 'blindTime': 25.71, 'plants': 0, 'defuses': 0
        }

    def test_player_parsing(self) -> None:
        player_data = PlayerData(json_data=self.example_json)
        self.assertIsNotNone(player_data)
