class Game:

    def __init__(self):
        self.team1roundswon = 0
        self.team2roundswon = 0

    def setMap(self, map):
        self.map = map

    def setDate(self, date):
        self.date = date

    def setMatchpage(self, faceit):
        self.matchpage = faceit

    def setTeam1(self, team1):
        self.team1 = team1

    def setTeam2(self, team2):
        self.team2 = team2

    def setTeam1RoundsWon(self, team1rounds):
        self.team1roundswon = team1rounds
        self.roundsplayed = self.team1roundswon + self.team2roundswon

    def setTeam2RoundsWon(self, team2rounds):
        self.team2roundswon = team2rounds
        self.roundsplayed = self.team1roundswon + self.team2roundswon

    def printGame(self):
        print(self.map)
        print(self.date)
        print(self.matchpage)
        print("Team 1 -", self.team1roundswon)
        for player in self.team1:
            print(player.name)
        print("Team 2 -", self.team2roundswon)
        for player in self.team2:
            print(player.name)

