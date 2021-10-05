class Series:

    def __init__(self):
        self.games = []
        self.totalrounds = 0
        self.team1 = []
        self.team2 = []
        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []
        self.player5 = []
        self.player6 = []
        self.player7 = []
        self.player8 = []
        self.player9 = []
        self.player10 = []
        self.player11 = []
        self.player12 = []


    def addGame(self, game):
        self.games.append(game)

    def createTeams(self):
        self.totalrounds = 0
        for game in self.games:
            self.totalrounds += game.roundsplayed
        for game in self.games:
            for player in game.team1 + game.team2:
                if not self.player1 or player in self.player1:
                    self.player1.append(player)
                elif not self.player2 or player in self.player2:
                    self.player2.append(player)
                elif not self.player3 or player in self.player3:
                    self.player3.append(player)
                elif not self.player4 or player in self.player4:
                    self.player4.append(player)
                elif not self.player5 or player in self.player5:
                    self.player5.append(player)
                elif not self.player6 or player in self.player6:
                    self.player6.append(player)
                elif not self.player7 or player in self.player7:
                    self.player7.append(player)
                elif not self.player8 or player in self.player8:
                    self.player8.append(player)
                elif not self.player9 or player in self.player9:
                    self.player9.append(player)
                elif not self.player10 or player in self.player10:
                    self.player10.append(player)
                elif not self.player11 or player in self.player11:
                    self.player11.append(player)
                elif not self.player12 or player in self.player12:
                    self.player12.append(player)










