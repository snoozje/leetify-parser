import os
from bs4 import BeautifulSoup
from Player import Player
from Game import Game
from Stat import Stat
from Series import Series
import unicodecsv as csv

htmls = ["Drexel-vertigo.html", "Drexel-mirage.html"]
neublack = ["We1Dg-iwnl-", "Cubostar", "Pwniez", "TonySheng", "melonwater", "Solome6", "Snooz12", "NoodleArmss", "Snoozje", "melonæ°´"]

def processPlayerRow(playerRow, gameID, players, team, rounds):
    playerName = playerRow.contents[0].contents[0].span.string.strip()


    #if playerName not in neublack:
       #return

    currentPlayer = None
    for player in players:
        if (player.name == playerName) or (player.name == "Snooz12" and playerName == "Snoozje") or (player.name == "Snoozje" and playerName == "Snooz12") or (player.name == "melonwater" and playerName == "melonæ°´") or (player.name == "melonæ°´" and playerName == "melonwater"):
            currentPlayer = player

    if currentPlayer is None:
        currentPlayer = Player(playerName)
        currentPlayer.team = team
        players.append(currentPlayer)

    currentPlayer.addStats(createStat(playerRow, gameID, rounds))


def createStat(playerRow, gameID, rounds):
    currentStat = Stat()
    playerData = playerRow.contents

    try:
        currentStat.setKills(playerData[1].string)
        currentStat.setAssists(playerData[2].string)
        currentStat.setDeaths(playerData[3].string)
        currentStat.setKD(playerData[5].string)
        currentStat.setADR(playerData[6].string)
        currentStat.setHSP(playerData[7].string)
        currentStat.setLeetifyRating(playerData[12].string)
        currentStat.setHLTVRating(playerData[13].string)
        currentStat.setRoundsPlayed(rounds)
        currentStat.setGameID(gameID)
    except:
        pass
    return currentStat


def createGame(html, players=[]):
    # gameID = url.rsplit('/', 1)[-1]
    gameID = ""
    # req = requests.Session().get(url)
    # content = req.text

    with open(html, 'r') as f:
        file_content = f.read()  # Read whole file in the file_content string

    soup = BeautifulSoup(file_content, features="html.parser")

    playerRows = soup.find_all('tr')

    currentgame = Game()
    currentgame.setID(gameID)

    map = soup.find(class_="font-weight-bold mb-0").string
    currentgame.setMap(map)

    date = soup.find(class_="mb-0 text-muted").string
    currentgame.setDate(date)

    if soup.find(class_="mt-0 font-weight-bold mb-0 ml-1 datasource-link ng-star-inserted") is None:
        currentgame.setMatchpage("Matchmaking Game")
    else:
        matchpage = soup.find(class_="mt-0 font-weight-bold mb-0 ml-1 datasource-link ng-star-inserted")['href']
        currentgame.setMatchpage(matchpage)

    score = soup.find(class_="mb-0 mx-3").string
    scores = score.split(':')
    currentgame.setTeam1RoundsWon(int(scores[0]))
    currentgame.setTeam2RoundsWon(int(scores[1]))
    team = None
    for playerRow in playerRows:
        # only team headers have class, so we know it is a team
        # not a player named 'Team A'
        # needs more logic for series, in the event that A and B are
        # swapped between matches
        if playerRow.contents[0].get('class') is not None:
            if playerRow.contents[0].contents[0].strip() == 'Team A':
                team = 1
            else:
                team = 2
        else:
            processPlayerRow(playerRow, gameID, players, team, currentgame.roundsplayed)

    currentgame.getTeamsFromPlayers(players)

    return currentgame


def createSeries(gameHTMLs):
    series = Series()


    #gameHTMLs = []
    #map = "overpass"
    """
    for root, directories, files in os.walk("./Leetify/FCOL"):
        for filename in files:
            #if map in filename:
                filepath = os.path.join(root, filename)
                gameHTMLs.append(filepath)
    
    for root, directories, files in os.walk("./Leetify/NACE"):
        for filename in files:
            #if map in filename:
                filepath = os.path.join(root, filename)
                gameHTMLs.append(filepath)
    
    for root, directories, files in os.walk("./Leetify/SCRIM"):
        for filename in files:
            #if map in filename:
                filepath = os.path.join(root, filename)
                gameHTMLs.append(filepath)
    """
    for html in gameHTMLs:
        series.addGame(createGame(html, series.players))
    #print(f"{map} : {len(gameHTMLs)}")
    series.printSeries()
    return series


def createCSV(series):
    with open('series.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile)

        filewriter.writerow(['', 'K', 'A', 'D', '+/-', 'K/D', 'ADR', 'HS%', 'LR', 'HLTV'])
        for player in series.team1:
            stats = player.totalstats
            filewriter.writerow([str(player.name), str(stats.kills), str(stats.assists), str(stats.deaths),
                                 str(stats.kills - stats.deaths), str(stats.kdratio), str(stats.adr), str(stats.hsp),
                                 str(stats.leetifyR), str(stats.hltvR)])

        filewriter.writerow([''])

        for player in series.team2:
            stats = player.totalstats
            filewriter.writerow([str(player.name), str(stats.kills), str(stats.assists), str(stats.deaths),
                                 str(stats.kills - stats.deaths), str(stats.kdratio), str(stats.adr), str(stats.hsp),
                                 str(stats.leetifyR), str(stats.hltvR)])


if __name__ == '__main__':
    currentSeries = createSeries(htmls)
    createCSV(currentSeries)
