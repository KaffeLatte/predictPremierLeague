#coding: UTF-8
import numpy as np
import pylab as pl
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
import dataExtraction

from sklearn.linear_model import LogisticRegression

class LogisticRegressionModel(object):

	def __init__(self):
		self.lrm = LogisticRegression()


class Team(object):
	"""
	Målskillnad: 

	Antal vunna matcher:
	Vunna - förlorade matcher:

	Skott
	Skott på mål
	Skott ribba/stolpe

	Hörnor

	Frispark

	Offsides

	Gula kort

	Röda kort

	Average odds
	"""


	def __init__(self, name):
		self.attributeList = [0] * 12
		self.name = name

	def getRecentGames(self):
		#Implement

	def aggGoalDiff(value):
		attributeList[0].add(value)

	def aggWonGames(self):
		attributeList[1].add(value)

	def aggWonLostDiff(self):
		attributeList[2].add(value)

	def aggShots(self):
		attributeList[3].add(value)

	def aggShotsOnGoal(self):
		attributeList[4].add(value)

	def aggShotsWoodwork(self):
		attributeList[5].add(value)

	def aggCorners(self):
		attributeList[6].add(value)

	def aggFouls(self):
		attributeList[7].add(value)

	def aggOffsides(self):
		attributeList[8].add(value)

	def aggYellowCards(self):
		attributeList[9].add(value)

	def aggRedCards(self):
		attributeList[10].add(value)

	def setOdds(self):
		attributeList[11].add(value)



def createTeams():
	list = dataExtraction.readStockDataFromFile("E0")

	for row in list:
		if teamMap.has_key(row[2]) != true:
			t = Team(row[2])
			teamMap[row[2]] = t
		if teamMap.has_key(row[3]) != true:
			t = Team(row[3])
			teamMap[row[3]] = t

		#aggregate values to home team
		teamMap[row[2]].aggGoalDiff(row[4]-row[5])
		won = 0
		if (row[6] == 'H')
			won = 1

		lost = 0
		if (row[6] == 'A')
			lost = 1

		teamMap[row[2]].aggWonGames(won)
		teamMap[row[2]].aggWonLostDiff(lost)
		teamMap[row[2]].aggShots(row[11])
		teamMap[row[2]].aggShotsOnGoal(row[13])
		teamMap[row[2]].aggShotsWoodwork(0)#N/A
		teamMap[row[2]].aggCorners(row[17])
		teamMap[row[2]].aggFouls(row[15])
		teamMap[row[2]].aggOffsides(0)#N/A
		teamMap[row[2]].aggYellowCards(row[19])
		teamMap[row[2]].aggRedCards(row[21])
		teamMap[row[2]].setOdds()#function for average odds

		#aggregate values to away team
		teamMap[row[3]].aggGoalDiff(-1*(row[4]-row[5]))
		teamMap[row[3]].aggWonGames(lost)
		teamMap[row[3]].aggWonLostDiff(won)
		teamMap[row[3]].aggShots(row[12])
		teamMap[row[3]].aggShotsOnGoal(row[14])
		teamMap[row[3]].aggShotsWoodwork(0)#N/A
		teamMap[row[3]].aggCorners(row[18])
		teamMap[row[3]].aggFouls(row[16])
		teamMap[row[3]].aggOffsides(0)#N/A
		teamMap[row[3]].aggYellowCards(row[20])
		teamMap[row[3]].aggRedCards(row[22])
		teamMap[row[3]].setOdds()#function for average odds



teamMap = dict()

lrm = LogisticRegressionModel()


print list[1]
#print list[2]