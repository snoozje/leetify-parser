class Series:

    def __init__(self):
        self.games = []
        self.totalrounds = 0
        self.players = []
        self.team1 = []
        self.team2 = []


    def addGame(self, game):
        self.games.append(game)
        self.createTeams()

    def createTeams(self):
        self.totalrounds = 0
        for game in self.games:
            self.totalrounds += game.roundsplayed
        for game in self.games:
            for player in game.team1:
                if player not in self.team1:
                    self.team1.append(player)
            for player in game.team2:
                if player not in self.team2:
                    self.team2.append(player)

    def printSeries(self):
        print(self.totalrounds, " round series")
        print("Team 1 -")
        for player in self.team1:
            print(player.name)
        print("Team 2 -")
        for player in self.team2:
            print(player.name)
        for game in self.games:
            game.printShortGame()
