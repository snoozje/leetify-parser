from bs4 import BeautifulSoup
from Player import Player
from Game import Game
from Stat import Stat
from Series import Series
import requests
import csv

ncc1 = "https://beta.leetify.com/public/match-details/e481b6ab-5b67-44f9-9737-350b3b032971"
ncc2 = "https://beta.leetify.com/public/match-details/c4678f10-398f-4190-b8ef-a9ed385c0f86"

neur1 = "https://beta.leetify.com/public/match-details/93a1adc9-5ae3-452f-80ec-1140955d7056"
neur2 = "https://beta.leetify.com/public/match-details/6072193e-43b7-4f6b-ae3a-262869bbcb9a"

toothpaste1 = "https://beta.leetify.com/public/match-details/000b315a-fc4d-4999-9f2e-3d2988828ec7"
toothpaste2 = "https://beta.leetify.com/public/match-details/d5425718-e52c-4667-baac-1740bf932d36"


urls = [toothpaste1, toothpaste2]


def processPlayerRow(playerRow, gameID, players, team, rounds):
    playerName = playerRow.contents[0].contents[0].span.string.strip()
    currentPlayer = None
    for player in players:
        if player.name == playerName:
            currentPlayer = player

    if currentPlayer == None:
        currentPlayer = Player(playerName)
        currentPlayer.team = team
        players.append(currentPlayer)

    currentPlayer.addStats(createStat(playerRow, gameID, rounds))


def createStat(playerRow, gameID, rounds):
    currentStat = Stat()
    playerData = playerRow.contents

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
    return currentStat


"""
def createPlayer(playerRow):
    playerName = playerRow.contents[0].contents[0].span.string.strip()
    currentPlayer = Player(playerName)
    playerData = playerRow.contents

    currentPlayer.setKills(playerData[1].string)
    currentPlayer.setAssists(playerData[2].string)
    currentPlayer.setDeaths(playerData[3].string)
    currentPlayer.setKD(playerData[5].string)
    currentPlayer.setADR(playerData[6].string)
    currentPlayer.setHSP(playerData[7].string)
    currentPlayer.setLeetifyRating(playerData[12].string)
    currentPlayer.setHLTVRating(playerData[13].string)
    return currentPlayer
"""


def createGame(url, players=[]):
    gameID = url.rsplit('/', 1)[-1]
    req = requests.get(url)
    content = req.text
    soup = BeautifulSoup(content, features="html.parser")
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
    # print(score)
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


def createSeries(gamesUrls):
    series = Series()
    for game in gamesUrls:
        series.addGame(createGame(game, series.players))
    series.printSeries()
    return series


def createCSV(series):
    with open('series.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)

        filewriter.writerow(['', 'K', 'A', 'D', '+/-', 'K/D', 'ADR', 'HS%', 'LR', 'HLTV'])
        for player in series.team1:
            stats = player.totalstats
            filewriter.writerow([str(player.name), str(stats.kills), str(stats.assists), str(stats.deaths),
                                 str(stats.kills - stats.deaths), str(stats.kdratio), str(stats.adr), str(stats.hsp),
                                 str(stats.leetifyR), str(stats.hltvR)])

        filewriter.writerow([])

        for player in series.team2:
            stats = player.totalstats
            filewriter.writerow([str(player.name), str(stats.kills), str(stats.assists), str(stats.deaths),
                                 str(stats.kills - stats.deaths), str(stats.kdratio), str(stats.adr), str(stats.hsp),
                                 str(stats.leetifyR), str(stats.hltvR)])


def main():
    currentSeries = createSeries(urls)
    createCSV(currentSeries)


if __name__ == '__main__':
    main()
