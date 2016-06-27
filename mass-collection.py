import sys
import requests
import csv
import math
import heapq
import time
from itertools import chain, combinations
from bs4 import BeautifulSoup


dates = []
year = 4000
months = [11,12,1,2,3,4]
for x in range(2013,2017):
    for y in range(0,6):
        for z in range(1,31):
            month = str(months[y])
            day = str(z)
            year = str(x)
            base_url = "http://www.sports-reference.com/cbb/boxscores/index.cgi?month="
            base_url = base_url + month + "&day=" + day + "&year=" + year
            dates.append(base_url)



spreads = []
assists = []
steals = []
blocks = []
personal_fouls = []
eff_fg_percentage = []
count = 0
for link in dates:
    count = count + 1
    print count
    print link
    print len(spreads)
    print "\n"

    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    all_games = soup.findAll('table', class_="no_highlight")
    for index in range(0, len(all_games)):
        temp_assists = []
        temp_steals = []
        temp_blocks = []
        temp_pfs = []
        temp_eff_fg = []
        if (index % 4) == 0:
            string = str(all_games[index])
            string1 = string.partition('"align_right">')[2]
            string2 = string1.partition('</td')
            score1 = string2[0]
            string3 = string2[2].partition('"align_right">')[2]
            score2 = string3.partition('</td')[0]
            if not score1 or not score2:
                break

            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            box = soup.findAll('table', class_="no_highlight")
            string = str(box[index])
            string = string.partition('"align_right bold_text"><a href="')[2]
            string = string.partition('">Final')[0]
            base_url = "http://www.sports-reference.com"
            box_score_link = base_url + string


            if box_score_link != "http://www.sports-reference.com":
                r = requests.get(box_score_link)
                soup = BeautifulSoup(r.text, "html.parser")
                efg = soup.findAll('tr', class_="stat_total")
                string = str(efg[1])
                for x in range (0,3):
                    string = string.partition('"right">')[2]
                eff_fg_1 = string.partition('</td')[0]
                if not eff_fg_1:
                    break

                string = str(efg[3])
                for x in range (0,3):
                    string = string.partition('"right">')[2]
                eff_fg_2 = string.partition('</td')[0]
                if not eff_fg_2:
                    break

                soup = BeautifulSoup(r.text, "html.parser")
                ast = soup.findAll('tr', class_="bold_text stat_total")
                string = str(ast[0])
                for x in range (0,21):
                    string = string.partition('"right">')[2]
                    if x == 16:
                        assist1 = string.partition('</td')[0]
                        if not assist1:
                            break
                    if x == 17:
                        steals1 = string.partition('</td')[0]
                        if not steals1:
                            break
                    if x == 18:
                        blocks1 = string.partition('</td')[0]
                        if not blocks1:
                            break
                pfs1 = string.partition('</td')[0]
                if not pfs1:
                    break

                string = str(ast[1])
                for x in range (0,21):
                    string = string.partition('"right">')[2]
                    if x == 16:
                        assist2 = string.partition('</td')[0]
                        if not assist2:
                            break
                    if x == 17:
                        steals2 = string.partition('</td')[0]
                        if not steals2:
                            break
                    if x == 18:
                        blocks2 = string.partition('</td')[0]
                        if not blocks2:
                            break
                pfs2 = string.partition('</td')[0]
                if not pfs2:
                    break

                temp_assists.append(float(assist1))
                temp_assists.append(float(assist2))
                assists.append(temp_assists)
                temp_steals.append(float(steals1))
                temp_steals.append(float(steals2))
                steals.append(temp_steals)
                temp_blocks.append(float(blocks1))
                temp_blocks.append(float(blocks2))
                blocks.append(temp_blocks)
                temp_pfs.append(float(pfs1))
                temp_pfs.append(float(pfs2))
                personal_fouls.append(temp_pfs)
                temp_eff_fg.append(float(eff_fg_1))
                temp_eff_fg.append(float(eff_fg_2))
                eff_fg_percentage.append(temp_eff_fg)
                spreads.append(float(score1) - float(score2))

                with open("output.csv", "wb") as f:
                    writer = csv.writer(f)
                    if len(spreads) > 0:
                        for x in range(0, len(spreads)):
                            for y in assists[x]:
                                writer.writerow([y])
                            for y in steals[x]:
                                writer.writerow([y])
                            for y in blocks[x]:
                                writer.writerow([y])
                            for y in personal_fouls[x]:
                                writer.writerow([y])
                            for y in eff_fg_percentage[x]:
                                writer.writerow([y])

                            writer.writerow([spreads[x]])
