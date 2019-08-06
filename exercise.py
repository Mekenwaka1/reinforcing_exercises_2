import operator


ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]


contestants = {
"Smudge": 0,
"Tigger":0,
"Simba": 0,
"Bella": 0,
"Lucky": 0,
"Boots": 0,
"Felix": 0}


contestants_names = contestants.keys()
for ballot in ballots: 

    if( ballot["gold"] in contestants_names):
        contestants[ballot["gold"]] += 3
    if( ballot["silver"] in contestants_names):
        contestants[ballot["silver"]] += 2
    if( ballot["bronze"] in contestants_names):
        contestants[ballot["bronze"]] += 1

# print(contestants)
print(max(contestants.items(), key=operator.itemgetter(1))[0] + " won.")