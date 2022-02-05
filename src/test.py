import requests

from src.Player import Player
from src.Stat import Stat

if __name__ == '__main__':

    url1 = "https://api.leetify.com/api/games/b21c0b62-b61f-4020-bae3-db9bafa10d62"
    url2 = "https://api.leetify.com/api/games/d6c37427-d5ee-497e-80d8-2386f5e4a817"

    game1 = requests.request("GET", url1)
    game2 = requests.request("GET", url1)

    data2 = game2.json()
    playerStats2 = data2['playerStats']

    data1 = game1.json()
    playerStats1 = data1['playerStats']

    for i in range(0, 10):
        player = playerStats1[i]

        currentPlayer = Player(player['name'])
        currentStat = Stat()

        currentStat.setKills(player['totalKills'])
        currentStat.setAssists(player['totalAssists'])
        currentStat.setDeaths(player['totalDeaths'])
        currentStat.setKD(player['kdRatio'])
        currentStat.setADR(player['dpr'])
        currentStat.setHSPFloat(player['hsp'])
        currentStat.setLeetifyRating(player['leetifyRating']*100)
        currentStat.setHLTVRating(player['hltvRating'])
        currentStat.setRoundsPlayed(player['tRoundsLost'] + player['ctRoundsLost'] +
                                    player['tRoundsWon'] + player['ctRoundsWon'])
        currentStat.setGameID(player['gameId'])

        currentPlayer.addStats(currentStat)
        currentPlayer.calculateTotalStats()
        currentPlayer.printPlayer()


