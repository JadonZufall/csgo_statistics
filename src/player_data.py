

class PlayerData:
    def __init__(self, json_data: dict) -> None:
        # Player data
        self._steam_id = json_data["steamID"]
        self._player_name = json_data["playerName"]
        self._team_name = json_data["teamName"]

        # KDA data
        self._kills = json_data["kills"]
        self._deaths = json_data["deaths"]
        self._assists = json_data["assists"]
        self._kdr = json_data["kdr"]                    # Kill death ratio
        self._adr = json_data["adr"]                    # Average damage round

        # More kill data
        self._trade_kills = json_data["tradeKills"]     # Traded kills
        self._team_kills = json_data["teamKills"]       # Team kills
        self._suicides = json_data["suicides"]          # Self kills

        # Damage data
        self._damage_done = json_data["totalDamageGiven"]           # Damage done to enemy
        self._damage_taken = json_data["totalDamageTaken"]          # Damage taken
        self._team_damage = json_data["totalTeamDamageGiven"]       # Damage done to friendly

        # Gunplay data
        self._total_shots = json_data["totalShots"]
        self._total_hits = json_data["shotsHit"]
        self._accuracy = json_data["accuracy"]
        self._rating = json_data["rating"]

        # Percentage of rounds where the player got a kill, assist, survived or was traded.
        self._kast = json_data["kast"]

        self._head_shots = json_data["hs"]
        self._head_shot_perc = json_data["hsPercent"]

        self._first_bloods = json_data["firstKills"]
        self._died_first = json_data["firstDeaths"]

        self._bomb_plants = json_data["plants"]
        self._bomb_defuses = json_data["defuses"]

        # Utility data
        # Utility damage
        self._ud = json_data["utilityDamage"]

        # Smoke Data
        self._smokes_thrown = json_data["smokesThrown"]

        # Flash bang data
        self._flashes_thrown = json_data["flashesThrown"]
        self._flash_assists = json_data["flashAssists"]
        self._enemies_flashed = json_data["enemiesFlashed"]
        self._friendly_flashed = json_data["teammatesFlashed"]
        self._blind_time = json_data["blindTime"]

        # High Explosive data
        self._he_thrown = json_data["heThrown"]

        # Molotov data
        self._fire_thrown = json_data["fireThrown"]

    @property
    def player_name(self) -> str:
        return self._player_name
