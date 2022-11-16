from typing import Union


class RoundData:
    def __init__(self, json_data: dict) -> None:
        # Round Information
        self._round_number: int = json_data["roundNum"]
        self._start_tick: int = json_data["startTick"]
        self._freeze_end: int = json_data["freezeTimeEndTick"]
        self._end_tick: int = json_data["endTick"]
        self._last_tick: int = json_data["endOfficialTick"]

        # Objective
        self._bomb_plant_tick: int = json_data["bombPlantTick"]
        self._bomb_planted: bool = json_data["bombPlanted"]
        self._bomb_site: str = json_data["bombsite"]
        self._plant_pos: dict[str, int] = json_data["bomb"]

        # Scoring
        self._t_score: int = json_data["tScore"]
        self._ct_score: int = json_data["ctScore"]
        self._end_t_score: int = json_data["endTScore"]
        self._end_ct_score: int = json_data["endCTScore"]
        self._t_team_name: str = json_data["tTeam"]
        self._ct_team_name: str = json_data["ctTeam"]
        self._winning_side: str = json_data["winningSide"]
        self._winning_team: str = json_data["winningTeam"]
        self._losing_team: str = json_data["losingTeam"]
        self._round_end_reason: str = json_data["roundEndReason"]

        # Economy
        self._t_spending: int = json_data["tRoundSpendMoney"]
        self._ct_spending: int = json_data["ctRoundSpendMoney"]
        self._t_buy_type: str = json_data["tBuyType"]
        self._ct_buy_type: str = json_data["ctBuyType"]

        # Players [{"playerName": _____, "steamID": _____}, ...]
        self._t_players: list[dict[str, Union[str, int]]] = json_data["tSide"]["players"]
        self._ct_players: list[dict[str, Union[str, int]]] = json_data["ctSide"]["players"]

        # Round information
        self._kills: list[dict] = json_data["kills"]
        self._damages: list[dict] = json_data["damages"]
        self._grenades: list[dict] = json_data["grenades"]
        self._flashes: list[dict] = json_data["flashes"]
        self._fires: list[dict] = json_data["fires"]
        self._smokes: list[dict] = json_data["smokes"]
        self._projectiles = list[dict] = json_data["projectiles"]
        self._bomb_events: list[dict] = json_data["bombEvents"]
        self._weapon_fires: list[dict] = json_data["weaponFires"]
        self._frames: list[dict] = json_data["frames"]

    @property
    def round_number(self) -> int:
        return self._round_number

    @property
    def start(self) -> int:
        return self._freeze_end

    @property
    def end(self) -> int:
        return self._last_tick

    @property
    def t_win(self) -> bool:
        return self._winning_side == "T"

    @property
    def ct_win(self) -> bool:
        return self._winning_side == "CT"

    @property
    def t_score(self) -> int:
        return self._t_score

    @property
    def ct_score(self) -> int:
        return self._ct_score
