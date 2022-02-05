import os

from bs4 import BeautifulSoup
import requests

from src.Match import Match
from src.Team import Team


# TODO: find a better way to link team name to the html file, or get html dynamically
faceit = {
    "NEU BLACK": "./FACEIT/NEU Black.html",
    "UARK ESPORTS": "./FACEIT/UARK Esports.html",
    "RIT CS BLACK": "./FACEIT/RIT CS Black.html",
    "UOFT JVM": "./FACEIT/UofT JVM.html",
    "FIU GOLD": "./FACEIT/FIU Gold.html",
    "RU JV WHITE": "./FACEIT/RU JV White.html",
    "UMASS AMHERST JV": "./FACEIT/UMass Amherst JV.html",
    "WESTERNU": "./FACEIT/Western U.html",
    "BLUE DEMONS": "./FACEIT/Blue Demons.html"
}


"""
Get the team names, date, and map scores into a match object
"""
def processMatch(matchrow):
    # team1name = matchrow.contents[1].contents[0].contents[0].contents[2].strip()
    # team2name = matchrow.contents[3].contents[0].contents[0].contents[2].strip()

    date = matchrow.find(class_="start-time").string

    teamnames = matchrow.find_all(class_="info")

    try:
        team1name = teamnames[0].contents[2].strip()
    except:
        team1name = "UC CSGO White"
    try:
        team2name = teamnames[1].contents[2].strip()
    except:
        team2name = "UC CSGO White"
    # print(team1name + team2name)

    if team1name == 'BYE':
        team1score = 2
        team2score = 0
    elif team2name == 'BYE':
        team2score = 2
        team1score = 0
    else:
        team1score = matchrow.contents[1].find(class_="team-score").string
        team2score = matchrow.contents[3].find(class_="team-score").string

    currentMatch = Match(team1name, team2name, team1score, team2score, date)
    # currentMatch.printMatch()
    return currentMatch


"""
Iterate over all matches in a round and puts the matches in a list
"""
def processRound(file):
    with open(file, 'r') as f:
        file_content = f.read()

    soup = BeautifulSoup(file_content, features="html.parser")

    matchrows = soup.find_all(class_="mat-row cdk-row ng-star-inserted")
    matchrows.pop()

    matches = []

    for matchrow in matchrows:
        matches.append(processMatch(matchrow))
    return matches


"""
If maps played on the faceit team stats page have the same date as a NACE match, assume they are corresponding
Uses NACE page positioning to determine map pick (left side/team1 picks first)
Assumes that no other maps were played on the same date by the team
"""
def parseFaceit(html, curTeam):

    curName = curTeam.name.upper()
    curMatches = curTeam.matches

    with open(html, 'r') as f:
        file_content = f.read()  # Read whole file in the file_content string

    soup = BeautifulSoup(file_content, features="html.parser")

    matchrow = soup.find_all(class_="match-history-stats__row")
    matchrow.pop(0)

    # map = match.contents[10].contents[1].contents[1].string

    for NACEmatch in curMatches:
        faceitMatches = []
        for match in matchrow:
            date = match.contents[1].string.split()[0]
            if int(date.split('/')[1]) < 10 or int(date.split('/')[2]) != 2021:
                continue
            if date == NACEmatch.date:
                mapandwon = []
                de_map = match.contents[10].contents[1].contents[1].string
                won = match.contents[6].contents[1].contents[1].string
                mapandwon.append(de_map)
                mapandwon.append(won)
                faceitMatches.append(mapandwon)

        faceitMatches.reverse()

        if len(faceitMatches) >= 2:
            if NACEmatch.team1name.upper() == curName:
                curTeam.mapsPicked[faceitMatches[0][0]] += 1
            elif NACEmatch.team2name.upper() == curName:
                curTeam.mapsPicked[faceitMatches[1][0]] += 1

        for mapdata in faceitMatches:
            curTeam.mapsPlayed[mapdata[0]] += 1
            if mapdata[1].upper().strip() == 'WIN':
                curTeam.mapsWon[mapdata[0]] += 1


"""
Tries to create the specified team by collecting all matches they were in
Parses their FACEIT data if available
"""
def createTeam(teamname, rounds):
    curTeam = Team(teamname)
    found = False
    for round in rounds:
        for match in round:
            if match.team1name.upper() == teamname.upper() or match.team2name.upper() == teamname.upper():
                found = True
                curTeam.addMatch(match)

    if teamname.upper() in faceit:
        parseFaceit(faceit[teamname.upper()], curTeam)
    else:
        print("No Faceit data found")

    if not found:
        print("Team not found")

    return curTeam


if __name__ == '__main__':
    # req = requests.Session().get("https://cslesports.mainline.gg/nacestarleague/open/open-csgo/csgo-east/-/tournament/matches")
    # content = req.text
    # soup = BeautifulSoup(content, features="html.parser")
    # print(soup.prettify())

    roundHTMLs = []
    for root, directories, files in os.walk("./NACE Open East"):
        for filename in files:
            filepath = os.path.join(root, filename)
            roundHTMLs.append(filepath)


    for root, directories, files in os.walk("./NACE Open West"):
        for filename in files:
            filepath = os.path.join(root, filename)
            roundHTMLs.append(filepath)


    rounds = []

    for round in roundHTMLs:
        print(round)
        rounds.append(processRound(round))

    while True:
        print("enter team name or q to quit")
        teamname = input()
        if teamname == 'q':
            quit(0)
        teaminfo = createTeam(teamname, rounds)
        teaminfo.printTeam()
        print()
