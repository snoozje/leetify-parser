class Stat:

    def __init__(self):
        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.kdratio = 0
        self.adr = 0
        self.hsp = 0
        self.leetifyR = 0
        self.hltvR = 0
        self.roundsplayed = 0
        self.gameID = ""

    def setKills(self, kills):
        self.kills = int(kills)

    def setAssists(self, assists):
        self.assists = int(assists)

    def setDeaths(self, deaths):
        self.deaths = int(deaths)

    def setKD(self, kdratio):
        self.kdratio = float(kdratio)

    def setADR(self, adr):
        self.adr = float(adr)

    def setHSPFloat(self, hsp):
        self.hsp = hsp

    def setHSP(self, hsp):
        hs = hsp.split()
        self.hsp = int(hs[0])

    def setLeetifyRating(self, leetifyR):
        self.leetifyR = float(leetifyR)

    def setHLTVRating(self, hltvR):
        self.hltvR = float(hltvR)

    def setRoundsPlayed(self, rounds):
        self.roundsplayed = rounds

    def setGameID(self, gameID):
        self.gameID = gameID

    def printStat(self):
        """
        print("kills:", self.kills)
        print("assists:", self.assists)
        print("deaths:", self.deaths)
        print("KD:", self.kdratio)
        print("ADR:", self.adr)
        print("HS%:", self.hsp)
        print("Leetify Rating:", self.leetifyR)
        print("HLTV Rating:", self.hltvR)
        """
        print(self.kills, self.assists, self.deaths, self.kdratio, self.adr, self.hsp, self.leetifyR, self.hltvR)
