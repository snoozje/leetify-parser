import csv

import requests

from src.Player import Player
from src.Stat import Stat


def createCSV(players):
    with open('series.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)

        filewriter.writerow(['', 'K', 'A', 'D', '+/-', 'K/D', 'ADR', 'HS%', 'LR', 'HLTV'])

        for player in players:
            stats = player.totalstats
            filewriter.writerow([str(player.name), str(stats.kills), str(stats.assists), str(stats.deaths),
                                 str(stats.kills - stats.deaths), str(stats.kdratio), str(stats.adr), str(stats.hsp),
                                 str(stats.leetifyR), str(stats.hltvR)])

if __name__ == '__main__':

    urls = ["https://api.leetify.com/api/games/f68790d0-f0c2-422d-8316-16105c42bf47", "https://api.leetify.com/api/games/a27376b6-bd03-41ae-93f8-c931f06b10a9"]

    data = [requests.request("GET", url).json() for url in urls]

    player_names = {game_data['playerStats'][i]['name'] for i in range(0, 10) for game_data in data}

    players = []

    for player_name in player_names:
        currentPlayer = Player(player_name)

        for game_data in data:
            for player in game_data['playerStats']:
                if player['name'] != player_name:
                    continue

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
        players.append(currentPlayer)

    players.sort()
    for player in players:
        player.printPlayer()

    createCSV(players)



