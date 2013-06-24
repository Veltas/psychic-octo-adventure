import json
import operator
from pprint import pprint

with open('data.json') as data_file:    
  data = json.load(data_file)

gamesTable = {}

for x in data["data"]:
  for y in x["games"]:
    if y["name"] in gamesTable:
        gamesTable[y["name"]] += 1
    else:
        gamesTable[y["name"]] = 1	

maxDisplay = 6
sortedGames = sorted(gamesTable.iteritems(), key=operator.itemgetter(1), reverse=True)

#then just take the first 6 from this sortedGames list :)))

count=0

for popularity, game in enumerate(sortedGames):
  if count < maxDisplay:
    pprint(game)

