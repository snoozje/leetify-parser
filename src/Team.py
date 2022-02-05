class Team:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.matches = []
        self.mapsPlayed = {
            "de_inferno": 0,
            "de_mirage": 0,
            "de_dust2": 0,
            "de_nuke": 0,
            "de_overpass": 0,
            "de_vertigo": 0,
            "de_ancient": 0
        }
        self.mapsPicked = {
            "de_inferno": 0,
            "de_mirage": 0,
            "de_dust2": 0,
            "de_nuke": 0,
            "de_overpass": 0,
            "de_vertigo": 0,
            "de_ancient": 0
        }
        self.mapsWon = {
            "de_inferno": 0,
            "de_mirage": 0,
            "de_dust2": 0,
            "de_nuke": 0,
            "de_overpass": 0,
            "de_vertigo": 0,
            "de_ancient": 0
        }

    def sameName(self, name):
        return name is self.name

    def addMatch(self, match):
        self.matches.append(match)
        if match.team1name.upper() == self.name.upper():
            if match.team1score == 'W' or match.team1score > match.team2score or match.team2name == 'BYE':
                self.wins += 1
            else:
                self.losses += 1
        elif match.team2name.upper() == self.name.upper():
            if match.team2score == 'W' or match.team1score < match.team2score or match.team1name == 'BYE':
                self.wins += 1
            else:
                self.losses += 1

    def printTeam(self):
        print(self.name)
        print(str(self.wins) + "W-" + str(self.losses) + "L")
        for match in self.matches:
            if match.team1name.upper() == self.name.upper():
                print(match.team1score + "-" + match.team2score + " " + match.team2name)
            elif match.team2name.upper() == self.name.upper():
                print(match.team2score + "-" + match.team1score + " " + match.team1name)

        # TODO: iterate over dicts instead of hard coding everything
        print()
        print("Map Stats")
        print("Inferno: picked " + str(self.mapsPicked['de_inferno']) + " out of " + str(self.mapsPlayed['de_inferno']) + ", won " + str(self.mapsWon['de_inferno']))
        print("Mirage: picked " + str(self.mapsPicked['de_mirage']) + " out of " + str(self.mapsPlayed['de_mirage']) + ", won " + str(self.mapsWon['de_mirage']))
        print("Dust 2: picked " + str(self.mapsPicked['de_dust2']) + " out of " + str(self.mapsPlayed['de_dust2']) + ", won " + str(self.mapsWon['de_dust2']))
        print("Nuke: picked " + str(self.mapsPicked['de_nuke']) + " out of " + str(self.mapsPlayed['de_nuke']) + ", won " + str(self.mapsWon['de_nuke']))
        print("Overpass: picked " + str(self.mapsPicked['de_overpass']) + " out of " + str(self.mapsPlayed['de_overpass']) + ", won " + str(self.mapsWon['de_overpass']))
        print("Vertigo: picked " + str(self.mapsPicked['de_vertigo']) + " out of " + str(self.mapsPlayed['de_vertigo']) + ", won " + str(self.mapsWon['de_vertigo']))
        print("Ancient: picked " + str(self.mapsPicked['de_ancient']) + " out of " + str(self.mapsPlayed['de_ancient']) + ", won " + str(self.mapsWon['de_ancient']))

