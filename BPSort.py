#!/usr/bin/python

## This algorithm is not ready yet

# Sorting for BP
# Goals:
# -Sort algorithm, classes Sort, Site, SiteLeader, Volunteer
# -Import csv files using the python pkg 'csv'
# -Export csv files
# -Pickling to save sorts already performed and to allow prg to minimize changes between successive sorts


# Sort:
# 	Sites
#	SiteLeaders
# 	Volunteers


class Sort(object):
	self.Sites
	self.SiteLeaders
	self.Volunteers
	
	def __init__(self):
		self.Sites=[]
		self.SiteLeaders=[]
		self.Volunteers=[]
	
	# (for now?) the functions take only values relev to sorting
	def addSite(number,headcount,isOutdoor):
		self.Sites.append(new Site(number,headcount,isOutdoor))
		
class Site(object):
	self.id
	self.headcount
	self.siteleaders
	self.volunteers
	self.isOutdoor
	
	def __init__(number,headcount,isOutdoor):
		self.id=number
		self.headcount=headcount
		self.isOutdoor=isOutdoor
		self.siteleaders=[]
		self.volunteers=[]

# person class+ inheritance ?

class SiteLeader(object):
class Volunteer(object):