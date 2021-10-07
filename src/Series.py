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

    def getGameRoundsByID(self, gameID):
        for game in self.games:
            if game.gameID == gameID:
                return game.roundsplayed

    def printSeries(self):
        print(self.totalrounds, "round series")
        for player in self.team1:
            player.calculateTotalStats()
        for player in self.team2:
            player.calculateTotalStats()

        self.team1 = sorted(self.team1, reverse=True)
        self.team2 = sorted(self.team2, reverse=True)
        print("Team 1 -")
        for player in self.team1:
            print(player.name)
            player.printPlayer()
        print("Team 2 -")
        for player in self.team2:
            print(player.name)
            player.printPlayer()
        for game in self.games:
            game.printShortGame()
