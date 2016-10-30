#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json
import time
from datetime import datetime, date

# from pymongo import MongoClient
# client = MongoClient()
# db = client.locks

key = open('publickey').read()
base = 'https://eu.api.battle.net/wow/character/dun-modr/'

def charItems(name):
    logkey = '?fields=items&locale=en_GB&apikey=' + key
    url = base + name + logkey
    info = json.loads(urllib.urlopen(url).read())
    return info

def charFeed(name):
    logkey = '?fields=feed&locale=en_GB&apikey=' + key
    url = base + name + logkey
    info = json.loads(urllib.urlopen(url).read())
    return info

def charProg(name):
    logkey = '?fields=progression&locale=en_GB&apikey=' + key
    url = base + name + logkey
    info = json.loads(urllib.urlopen(url).read())
    return info

def charSttics(name):
    logkey = '?fields=statistics&locale=en_GB&apikey=' + key
    url = base + name + logkey
    info = json.loads(urllib.urlopen(url).read())
    return info


def date(stamp):
    dateStr = time.ctime(stamp/1000)
    return dateStr

def lastW():
    actual = datetime.today()
    gap = (actual.weekday()-2) # Miercoles es dia 2
    if gap < 0:
        gap = gap+7

    lastWeds = actual.replace(hour=9,minute=0, second=0,microsecond=0)
    lastWeds = long(time.mktime(lastWeds.timetuple())-86400*gap)*1000
    # resetDate = long(time.mktime(resetDate.timetuple()))*1000
    print "ULTIMA MIERCOLES: ", lastWeds
    return lastWeds

def checkReset():
    result = 0
    actual = datetime.today()
    if actual.weekday() == 2 and actual.hour >= 9 and actual.hour <= 10: # Miercoles es dia 2
        result = 1
    elif actual.weekday() == 2 and actual.hour >= 11:
        result = 2
    return result

def clearData():
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
    return general

def updateHTML(gen, lvls):
    htmlFile = open('datashow.html','w') # CAMBIAR DIRECTORIO!
    message = "<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><h3> Dofilock: Info saves </h3> Informacion sobre saves de cada player, datos extraidos de la api de battle net, por lo que es posible que la informacion no este 100% correcta/actualizada ya que los updates de blizzard no se realizan cada instante, ademas, hay eventos que se pueden perder en el feed que nos proporcionan. Disculpas por la representacion tan chapucera, es lo mas rapido funcional, sera mejorado.<br>"

    message = message + "<br><br> Mythics: "
    messUpd = ""
    for item in gen[0]:
        messUpd = messUpd + "<br>" + repr(item) + ": " + repr(gen[0][item])
    message = message + messUpd

    message = message + "<br><br> Raid TED Normal: "
    messUpd = ""
    for item in gen[1]:
        messUpd = messUpd + "<br>" + repr(item) + ": " + repr(gen[1][item])
    message = message + messUpd

    message = message + "<br><br> Raid TED Heroic: "
    messUpd = ""
    for item in gen[2]:
        messUpd = messUpd + "<br>" + repr(item) + ": " + repr(gen[2][item])
    message = message + messUpd

    message = message + "<br><br> NOTA: Si vuestro navegador cachea, pulsad F5 para actualizar... Este doc es un estático generado por script, chapucillas everywhere"
    # message = message + "<br><br> Last updates: "
    # messUpd = ""
    # for item in upd:
    #     messUpd = messUpd + "<br>" + repr(item) + ": " + repr(upd[item])
    # message = message + messUpd

    message = message + "<br><br> Member iLvls (Media máximo inventario - Media Equipado)"
    messUpd = ""
    for item in lvls:
        messUpd = messUpd + "<br>" + repr(item) + ": " + repr(lvls[item])
    message = message + messUpd

    htmlFile.write(message)
    htmlFile.close()

# MODE = 'FIRST'
MODE = 'MAN'


# A base datos......
miembros = ['Wizaras', 'Cuxulain', 'Lorzo', 'Nimro', 'Fudan', 'Palomitera', 'Odlarg', 'Megainho', 'Wizote', \
            'Khaelan', 'Llonganisa', 'Racknnar', 'Stiwie', 'Vaironn', 'Uborzz', 'Sàs', 'Yarako', 'Kaelan',
            'Druscaelan', 'Yakuka']
ilvls = dict()

for miembro in miembros:
    ilvls[miembro] = [0, 0]

if MODE == 'FIRST':
    clearData()

    lastUpd = dict()
    # db.insert_one()
    lastWeds = lastW()
    print 'salimos FIRST'

    MODE = 'MAN'

if MODE == 'MAN':
    with open('dataX.json', 'r') as fp:
        general = json.load(fp)
    print general

    instances = general[0]
    emeraldN = general[1]
    emeraldH = general[2]

    lastUpd = dict()
    # db.insert_one()
    lastWeds = lastW()
    print 'salimos MAN'

    flag = False

while 1:
    # db.find???
    if checkReset() == 1 and flag == False:
        flag = True
        general = clearData()
        instances = general[0]
        emeraldN = general[1]
        emeraldH = general[2]

        lastWeds = lastW()
        print 'Limpiando...'
    elif checkReset() == 2 and flag == True:
        flag = False
        print 'Reset flag limpia...'

    count = 0
    for miembro in miembros:
        try:

            # MYTHICS...
            a = charSttics(miembro)
            count = count + 1
            codigosInstanceApi = [2,5,8,11,16,17,20,23,26,27,28]
            print '> Counting dofito', count, 'of', len(miembros), '.....', miembro
            for i in codigosInstanceApi:
                # fecha mayor que ultimo miercoles?
                d = a['statistics']['subCategories'][5]['subCategories'][6]['statistics'][i]
                actual = d['lastUpdated']#+3*86400*1000
                # print d, lastWeds, date(actual), date(lastWeds)
                if actual > lastWeds:
                    try:
                        c = json.dumps(d['name']).split('(Mythic ')[1][:-2]
                        # print c
                        if miembro not in instances[c]:
                            instances[c].append(miembro)
                    except:
                        pass
                # raw_input()
            # lastUpd[miembro] = date(a['feed'][1]['timestamp'])


            # RAIDS...
            emerald = charProg(miembro)

            for n in range(7):
                if emerald['progression']['raids'][35]['bosses'][n]['normalTimestamp'] > lastWeds:
                    if miembro not in emeraldN[emerald['progression']['raids'][35]['bosses'][n]['name']]:
                        emeraldN[emerald['progression']['raids'][35]['bosses'][n]['name']].append(miembro)
                if emerald['progression']['raids'][35]['bosses'][n]['heroicTimestamp'] > lastWeds:
                    if miembro not in emeraldH[emerald['progression']['raids'][35]['bosses'][n]['name']]:
                        emeraldH[emerald['progression']['raids'][35]['bosses'][n]['name']].append(miembro)

            # KEYSTONES...

            # ITEM LEVEL...
            items = charItems(miembro)
            # print json.dumps(a)
            lvlM=items['items']['averageItemLevel']
            lvlE=items['items']['averageItemLevelEquipped']
            # print lvlM, lvlE

            ilvls[miembro][0] = lvlM
            ilvls[miembro][1] = lvlE


        except:
            print miembro, 'failed'


    print ' ~~~~~~~~~~~~ '
    print 'Mythic Basicas:'

    for instance in instances:
        print instance, ': ', instances[instance]

    print ' ~~~~~~~~~~~~ '
    print 'The Emerald Dream - Normal:'

    for instance in emeraldN:
        print instance, ': ', emeraldN[instance]

    print ' ~~~~~~~~~~~~ '
    print 'The Emerald Dream - Heroic:'

    for instance in emeraldH:
        print instance, ': ', emeraldH[instance]


    general = [instances, emeraldN, emeraldH]
    with open('dataX.json', 'w') as fp:
        json.dump(general, fp)

    # print ' ~~~~~~~~~~~~ '
    # print "Betrayers detection"
    # print "Betrayers de la semana en Mythic: ", betrayers

    # print ' ~~~~~~~~~~~~ '
    # print 'Ultima lectura:'
    #
    # for miembro in miembros:
    #     print miembro, lastUpd[miembro]


    updateHTML(general, ilvls)

    # db.update_one()
    # if martes:
    #     estado = 'CLEAR'
    time.sleep(300)

