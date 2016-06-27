import sys
import requests
import csv
import math
import heapq
import time
from itertools import chain, combinations
from bs4 import BeautifulSoup

selected_links = ['https://www.teamrankings.com/ncaa-basketball/stat/personal-fouls-per-game', 'https://www.teamrankings.com/ncaa-basketball/stat/steals-per-game', 'https://www.teamrankings.com/ncaa-basketball/stat/blocks-per-game', 'https://www.teamrankings.com/ncaa-basketball/stat/assists-per-game', 'https://www.teamrankings.com/ncaa-basketball/stat/effective-field-goal-pct']
# stat_links = []
# for link in selected_links:
#     string = "https://www.teamrankings.com/" + link
#     stat_links.append(string)

teams = []
intputs = []
y_values = [-14,10,-1,2]
y_index = 0

with open('mar13.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    teams = list(reader)


for game in teams:
    team_one_overall = 0.0
    team_two_overall = 0.0
    overall_temp = 0.0
    overall_scores = []
    overall_low_score = 0.0
    overall_high_score = 0.0
    last3_temp = 0.0
    last3_scores = []
    last3_low_score = 100.0
    last3_high_score = 0.0
    team_one = []
    team_two = []
    print "\n"
    for link in selected_links:
        time.sleep(.01)
        overall_scores = []
        last3_scores = []
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', class_="tr-table datatable scrollable")
        team_rows = table.findAll('tr')
        team_rows = team_rows[1:]
        for row in team_rows:
            overall_scores.append(float(row.findAll('td')[2].text.strip().replace("%", "")))
            last3_scores.append(float(row.findAll('td')[3].text.strip().replace("%", "")))


        overall_low_score = min(overall_scores)
        overall_high_score = max(overall_scores)
        last3_low_score = min(last3_scores)
        last3_high_score = max(last3_scores)

        for row in team_rows:
            if row.findAll('td')[1].text.strip() == game[0]:
                overall_temp = float(row.findAll('td')[2].text.strip().replace("%", ""))
                last3_temp = float(row.findAll('td')[3].text.strip().replace("%", ""))

                overall_temp = (overall_temp - overall_low_score) / (overall_high_score - overall_low_score)
                last3_temp = (last3_temp - last3_low_score) / (last3_high_score - last3_low_score)

                # print overall_temp
                # print last3_temp
                team_one.append(overall_temp)
                team_one.append(last3_temp)

                team_one_overall = team_one_overall + overall_temp + last3_temp

            if row.findAll('td')[1].text.strip() == game[1]:
                overall_temp = float(row.findAll('td')[2].text.strip().replace("%", ""))
                last3_temp = float(row.findAll('td')[3].text.strip().replace("%", ""))

                overall_temp = (overall_temp - overall_low_score) / (overall_high_score - overall_low_score)
                last3_temp = (last3_temp - last3_low_score) / (last3_high_score - last3_low_score)

                # print overall_temp
                # print last3_temp
                team_two.append(overall_temp)
                team_two.append(last3_temp)

                team_two_overall = team_two_overall + overall_temp + last3_temp


    # x = team_one_overall - team_two_overall
    # print x
    print "\n"
    for x in team_one:
        print x
    # print "\n"
    for x in team_two:
        print x
    print "\n"
    # print game[0]
    # print game[1]
    # print "\n"
    # print y_values[y_index]
    # y_index += 1
