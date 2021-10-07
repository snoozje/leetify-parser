from Stat import Stat


class Player:

    def __init__(self, name):
        self.name = name
        self.stats = []
        self.team = None
        self.totalstats = Stat()

    def setStats(self, stats):
        self.stats = stats

    def setTeam(self, team):
        self.team = team

    def addStats(self, stat):
        self.stats.append(stat)

    def calculateTotalStats(self):
        totalkills = 0
        totalassists = 0
        totaldeaths = 0
        totalKD = 0
        totaldamage = 0
        totalHSkills = 0
        totalLR = 0
        totalHLTVR = 0
        totalroundsplayed = 0

        for stat in self.stats:
            totalroundsplayed += stat.roundsplayed
            totalkills += stat.kills
            totalassists += stat.assists
            totaldeaths += stat.deaths
            totaldamage += stat.roundsplayed * stat.adr
            totalHSkills += int(stat.roundsplayed * stat.hsp)
            totalLR += stat.roundsplayed * stat.leetifyR
            totalHLTVR += stat.roundsplayed * stat.hltvR

        self.totalstats.setKills(totalkills)
        self.totalstats.setAssists(totalassists)
        self.totalstats.setDeaths(totaldeaths)
        self.totalstats.setKD(round(totalkills / totaldeaths, 2))
        self.totalstats.setADR(round(totaldamage / totalroundsplayed, 1))
        self.totalstats.setHSPFloat(round(totalHSkills / totalroundsplayed, 1))
        self.totalstats.setLeetifyRating(round(totalLR / totalroundsplayed, 2))
        self.totalstats.setHLTVRating(round(totalHLTVR / totalroundsplayed, 2))

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name

    def __lt__(self, other):
        return self.totalstats.hltvR - other.totalstats.hltvR < 0

    def __gt__(self, other):
        return self.totalstats.hltvR - other.totalstats.hltvR > 0

    def printPlayer(self):
        """
        print("name:", self.name)
        for stat in self.stats:
            stat.printStat()
        """
        self.totalstats.printStat()

