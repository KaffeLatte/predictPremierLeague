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
		self.matches = []

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
			t = Team()
			teamMap[row[2]] = t
		if teamMap.has_key(row[3]) != true:
			t = Team()
			teamMap[row[3]] = t

		#aggregate values to home team
		teamMap[row[2]].aggGoalDiff(row[4]-row[5])
		teamMap[row[2]].aggWonGames()
		teamMap[row[2]].aggWonLostDiff()
		teamMap[row[2]].aggShots()
		teamMap[row[2]].aggShotsOnGoal()
		teamMap[row[2]].aggShotsWoodwork()
		teamMap[row[2]].aggCorners()
		teamMap[row[2]].aggFouls()
		teamMap[row[2]].aggOffsides()
		teamMap[row[2]].aggYellowCards()
		teamMap[row[2]].aggRedCards()
		teamMap[row[2]].setOdds()

		#aggregate values to away team
		teamMap[row[3]].aggGoalDiff(-1*(row[4]-row[5]))
		teamMap[row[3]].aggWonGames()
		teamMap[row[3]].aggWonLostDiff()
		teamMap[row[3]].aggShots()
		teamMap[row[3]].aggShotsOnGoal()
		teamMap[row[3]].aggShotsWoodwork()
		teamMap[row[3]].aggCorners()
		teamMap[row[3]].aggFouls()
		teamMap[row[3]].aggOffsides()
		teamMap[row[3]].aggYellowCards()
		teamMap[row[3]].aggRedCards()
		teamMap[row[3]].setOdds()



teamMap = dict()

lrm = LogisticRegressionModel()

t = Team()
t.getRecentGames()

print list[1]
#print list[2]