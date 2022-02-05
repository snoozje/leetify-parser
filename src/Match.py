class Match:

    def __init__(self, team1name, team2name, team1score, team2score, date):
        self.team1name = team1name
        self.team2name = team2name
        self.team1score = team1score
        self.team2score = team2score
        self.date = self.processDate(date)
        self.map1score = None
        self.map2score = None
        self.map3score = None

    def processDate(self, strDate):
        month = strDate.split()[0]
        day = strDate.split()[1]

        if int(day) < 10:
            day = "0" + day

        if month == "Oct":
            return day + "/10/2021"
        elif month == "Nov":
            return day + "/11/2021"

    def printMatch(self):
        print(self.team1name + " " + self.team1score + "-" + self.team2score + " " + self.team2name)
