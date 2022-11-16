from awpy.analytics.stats import player_stats
from src.player_data import PlayerData


class ReplayData:
    def __init__(self, json_data: dict, load_player_data=True, load_round_data=True) -> None:
        self._map: str = json_data["mapName"]
        self._tick_rate: int = json_data["tickRate"]
        self._play_back: int = json_data["playbackTicks"]
        self._round_starts: list[int] = json_data["matchPhases"]["roundStarted"]
        self._round_endings: list[int] = json_data["matchPhases"]["roundEnded"]
        self._round_full_starts: list[int] = json_data["matchPhases"]["roundFreezetimeEnded"]
        self._round_full_endings: list[int] = json_data["matchPhases"]["roundEndedOfficial"]
        self._match_start: list[int] = json_data["matchPhases"]["matchStart"]
        self._team_switch: list[int] = json_data["matchPhases"]["teamSwitch"]
        # self._place_names: list[str] = json_data["parsedPlaceNames"]
        self._comp_ranks: list[str] = json_data["matchmakingRanks"]
        self._round_data: list[dict] = json_data["gameRounds"]
        self._number_of_rounds: int = len(self._round_data)

        self._player_data: list[PlayerData] = []
        if load_player_data:
            player_data: dict[str, dict] = player_stats(json_data["gameRounds"], return_type="json")
            for value in player_data.values():
                print(value)
                self._player_data.append(PlayerData(json_data=value))
        self._number_of_players: int = len(self._player_data)

    def get_round_data(self, round_number: int) -> dict:
        return self._round_data[round_number]

    def get_player_by_index(self, index: int) -> PlayerData:
        return self._player_data[index]

    @property
    def number_of_rounds(self) -> int:
        return self._number_of_rounds

    @property
    def number_of_players(self) -> int:
        return self._number_of_players


