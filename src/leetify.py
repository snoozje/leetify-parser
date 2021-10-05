from bs4 import BeautifulSoup
from Player import Player
from Game import Game
import requests
url='https://beta.leetify.com/public/match-details/5191f7f6-d889-4ae8-958e-247cf8fe20f0'

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

def createGame(url):
    req = requests.get(url)
    content = req.text
    soup = BeautifulSoup(content, features="html.parser")
    playerrows = soup.find_all('tr')

    # remove non-player headers
    playerrows.pop(0)
    playerrows.pop(5)

    currentgame = Game()
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
    print(score)
    scores = score.split(':')
    currentgame.setTeam1RoundsWon(int(scores[0]))
    currentgame.setTeam2RoundsWon(int(scores[1]))

    players = []
    for player in playerrows:
        players.append(createPlayer(player))

    currentgame.setTeam1(players[0:5])
    currentgame.setTeam2(players[5:10])
    currentgame.printGame()

def createSeries(games):

    currentgame = Game()
    allplayerswithduplicates = []
    for game in games:
        currentgame.addGame(game)











