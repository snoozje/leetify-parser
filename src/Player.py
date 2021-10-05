class Player:

    def __init__(self, name):
        self.name = name
        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.kdratio = 0
        self.adr = 0
        self.hsp = 0
        self.leetifyR = 0
        self.hltvR = 0

    def setKills(self, kills):
        self.kills = kills

    def setAssists(self, assists):
        self.assists = assists

    def setDeaths(self, deaths):
        self.deaths = deaths

    def setKD(self, kdratio):
        self.kdratio = kdratio

    def setADR(self, adr):
        self.adr = adr

    def setHSP(self, hsp):
        self.hsp = hsp

    def setLeetifyRating(self, leetifyR):
        self.leetifyR = leetifyR

    def setHLTVRating(self, hltvR):
        self.hltvR = hltvR

    def __eq__(self, other):
        return self.name == other.name

    def printPlayer(self):
        print("name:", self.name)
        print("kills:", self.kills)
        print("assists:", self.assists)
        print("deaths:", self.deaths)
        print("KD:", self.kdratio)
        print("ADR:", self.adr)
        print("HS%:", self.hsp)
        print("Leetify Rating:", self.leetifyR)
        print("HLTV Rating:", self.hltvR)