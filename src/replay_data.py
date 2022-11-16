from awpy.analytics.stats import player_stats

from utils.linear_search import linear_search

from src.player_data import PlayerData
from src.round_data import RoundData


class ReplayData:
    def __init__(self, json_data: dict, load_player_data=True, load_round_data=True) -> None:
        # Game information
        self._map: str = json_data["mapName"]

        # Timing information
        self._tick_rate: int = json_data["tickRate"]
        self._play_back: int = json_data["playbackTicks"]

        # Round information
        self._round_starts: list[int] = json_data["matchPhases"]["roundStarted"]
        self._round_endings: list[int] = json_data["matchPhases"]["roundEnded"]

        # True round information
        self._round_full_starts: list[int] = json_data["matchPhases"]["roundFreezetimeEnded"]
        self._round_full_endings: list[int] = json_data["matchPhases"]["roundEndedOfficial"]

        # Game start tick and team switch tick
        self._match_start: list[int] = json_data["matchPhases"]["matchStart"][-1]
        self._team_switch: list[int] = json_data["matchPhases"]["teamSwitch"][-1]

        # Player competitive ranks
        self._comp_ranks: list[str] = json_data["matchmakingRanks"]

        # Parse player information into player data instances.
        self._player_data: list[PlayerData] = []
        if load_player_data:
            player_data: dict[str, dict] = player_stats(json_data["gameRounds"], return_type="json")
            for value in player_data.values():
                self._player_data.append(PlayerData(json_data=value))
        self._number_of_players: int = len(self._player_data)

        # Parse round information into round data instances.
        self._round_data: list[RoundData] = []
        if load_round_data:
            round_data: list[dict] = json_data["gameRounds"]
            for value in round_data:
                self._round_data.append(RoundData(json_data=value))
        self._number_of_rounds: int = len(self._round_data)

    def get_round_data(self, round_number: int) -> RoundData:
        return self._round_data[round_number]

    def get_player_by_index(self, index: int) -> PlayerData:
        return self._player_data[index]

    def get_player_by_name(self, player_name: str) -> PlayerData:
        index = linear_search([i.player_name for i in self._player_data], player_name)
        return self._player_data[index]

    @property
    def number_of_rounds(self) -> int:
        return self._number_of_rounds

    @property
    def number_of_players(self) -> int:
        return self._number_of_players


