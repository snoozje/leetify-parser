class Player:

    def __init__(self, name):
        self.name = name
        self.stats = []
        self.team = None

    def setStats(self, stats):
        self.stats = stats

    def setTeam(self, team):
        self.team = team

    def addStats(self, stat):
        self.stats.append(stat)

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name

    def printPlayer(self):
        print("name:", self.name)
        for stat in self.stats:
            stat.printStat()
