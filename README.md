# BB-HTML-Data-Collection

A set of python scripts using BeautifulSoup to extract basketball stats from HTML pages

There is a script for NCAA stats and NBA stats. Both collect the same stats -- personal fouls per game, steals per game, blocks per game, assists per game, and effective field goal percentage. The stats are collected from [TeamRankings](https://www.teamrankings.com/). The stats are from yearly averages and the last 3 games -- a total of 10 stats per team. 

The programs take two teams as arguments -- the teams in upcoming games. Therefore, the output of the program will be a total of 20 stats. There is the option to build a CSV file with games -- in the format of the example ``feb4 teams.csv``. The program will then parse all the games and output the 20 stats for each game. 

Each stat is normalized between 0 and 1 based on the min and maximum stats in the league for each stat. This is for later use of the statistics (for example feeding it into a neural network). By normalizing, each stat holds equal weight. 

There is also a script that does a mass collection of previous years NCAA basketball games. My current model collects stats from over 12,000 games. 

