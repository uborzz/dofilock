import json

instances = {'Arcway':list(), 'Black Rook Hold':list(), 'Vault of the Wardens':list(), 'Maw of Souls':list(), \
             'Halls of Valor':list(), "Neltharion's Lair":list(), 'Vault of the Wardens': list(), \
             'Eye of Azshara': list(), 'Darkheart Thicket':list(), 'Court of Stars': list(), 'Assault on Violet Hold':list()}
emeraldN = {'Nythendra':list(), 'Elerethe Renferal':list(), "Il'gynoth, Heart of Corruption":list(), 'Ursoc':list(), \
            'Dragons of Nightmare':list(), 'Cenarius':list(), 'Xavius':list()}
emeraldH = {'Nythendra':list(), 'Elerethe Renferal':list(), "Il'gynoth, Heart of Corruption":list(), 'Ursoc':list(), \
            'Dragons of Nightmare':list(), 'Cenarius':list(), 'Xavius':list()}
general = [instances, emeraldN, emeraldH]
with open('dataX.json', 'w') as fp:
    json.dump(general, fp)