import pandas as pd
import collections
import json

################################
def murderRateState():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse("Sheet1")
	# statesDict1 = dict()

	# allStates = df["State"]
	# for key in allStates:
	# 	if key in statesDict1:
	# 		statesDict1[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		statesDict1.update(s)

	# statesDict = list()
	# statesDict.append(statesDict1)
	# file = open("MurderRateState.js", "w+")
	# file.write(json.dumps(statesDict))
	# file.close()
	# print(statesDict)

	states_counter = collections.Counter(df['State'])
	output_dicts = [{'State': m, 'Freq': f} for m, f in states_counter.items()]
	file = open("MurderRateState.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()

################################

def murderRateDecState():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	year = df['Year']
	state = df['State']
	freq = dict()

	for i in range(0, len(df)):
		currYear = year.iloc[i]
		if(currYear >= 1980 and currYear < 1989):
			currDecade = 1980
		elif(currYear >= 1990 and currYear < 2000):
			currDecade = 1990
		elif(currYear >= 2000 and currYear < 2010):
			currDecade = 2000
		elif(currYear >= 2010):
			currDecade = 2010
		currState = state.iloc[i]
		if currDecade in freq:
			if currState in freq[currDecade]:
				freq[currDecade][currState] += 1
			else:
				key = {currState: 1}
				freq[currDecade].update(key)
		else:
			key = {currDecade:{currState: 1}}
			freq.update(key)

	#print(freq)

	file = open("MurderRateDecState.js", "w+")
	file.write(json.dumps(freq))
	file.close()

################################

def weaponRelationship():
	
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse("Sheet1")
	
        #stat_counter = collections.Counter(df['Relationship'])
	states_counter = collections.Counter(df['Weapon'])

	stat_counter = collections.Counter(df['Relationship'])
	output_dicts = [{'Relationship': i, 'Weapon': m, 'Frequency': f} for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("WeaponRelationship.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()

################################

def raceWeapon():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	"""race = df['Perpetrator Race']
	weapon = df['Weapon']
	freq = dict()

	for i in range(0, len(df)):
		currRace = race.iloc[i]
		currWeapon = weapon.iloc[i]
		if currRace in freq:
			if currWeapon in freq[currRace]:
				freq[currRace][currWeapon] += 1
			else:
				key = {currWeapon: 1}
				freq[currRace].update(key)
		else:
			key = {currRace:{currWeapon: 1}}
			freq.update(key)

	"""
	stat_counter = collections.Counter(df['Perpetrator Race'])
	states_counter = collections.Counter(df['Weapon'])
	output_dicts = [{'Perpetrator Race': i, 'Weapon': m, 'Frequency': f} for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("RaceWeapon.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()


################################

def murderPerpAge():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	age = df['Perpetrator Age']
	# freq = dict()

	# for key in age:
	# 	if key in freq:
	# 		freq[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		freq.update(s)

	# #print(freq)

	# file = open("MurderPerpAge.js", "w+")
	# file.write(json.dumps(freq))
	# file.close()

	freq1 = collections.Counter(df['Perpetrator Age'])
	freq = [{'Perpetrator Age': m, 'Freq': f} for m, f in freq1.items()]
	file = open("MurderPerpAge.js", "w+")
	file.write(json.dumps(freq))
	file.close()

################################

def murderRatePerpAgeDec():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	year = df['Year']
	age = df['Perpetrator Age']
	freq = dict()

	for i in range(0, len(df)):
		currYear = year.iloc[i]
		if(currYear >= 1980 and currYear < 1989):
			currDecade = 1980
		elif(currYear >= 1990 and currYear < 2000):
			currDecade = 1990
		elif(currYear >= 2000 and currYear < 2010):
			currDecade = 2000
		elif(currYear >= 2010):
			currDecade = 2010
		currAge = age.iloc[i]
		if currDecade in freq:
			if currAge in freq[currDecade]:
				freq[currDecade][currAge] += 1
			else:
				key = {currAge: 1}
				freq[currDecade].update(key)
		else:
			key = {currDecade:{currAge: 1}}
			freq.update(key)

	#print(freq)
	file = open("MurderRatePerpAgeDec.js", "w+")
	file.write(json.dumps(str(freq)))
	file.close()

################################

def murderPerpAgeState():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	"""age = df['Perpetrator Age']
	state = df['State']
	freq = dict()

	for i in range (0, len(df)):
		currState = state.iloc[i]
		currAge = age.iloc[i]
		if currState in freq:
			if currAge in freq[currState]:
				freq[currState][currAge] += 1
			else:
				key = {currAge: 1}
				freq[currState].update(key)
		else:
			key = {currState:{currAge:1}}
			freq.update(key)

	#print(freq)"""
	stat_counter = collections.Counter(df['Perpetrator Age'])
	states_counter = collections.Counter(df['State'])
	output_dicts = [{'Perpetrator Age': i, 'State': m, 'Frequency': f} for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("MurderPerpAgeState.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()

################################

def murderVicAge():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	# age = df['Victim Age']
	# freq = dict()

	# for key in age:
	# 	if key in freq:
	# 		freq[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		freq.update(s)

	#print(freq)
	freq1 = collections.Counter(df['Victim Age'])
	freq = [{'Victim Age': m, 'Freq': f} for m, f in freq1.items()]

	file = open("MurderVicAge.js", "w+")
	file.write(json.dumps(freq))
	file.close()

################################

def murderRateVicAgeDec():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	year = df['Year']
	age = df['Victim Age']
	freq = dict()

	for i in range(0, len(df)):
		currYear = year.iloc[i]
		if(currYear >= 1980 and currYear < 1989):
			currDecade = 1980
		elif(currYear >= 1990 and currYear < 2000):
			currDecade = 1990
		elif(currYear >= 2000 and currYear < 2010):
			currDecade = 2000
		elif(currYear >= 2010):
			currDecade = 2010
		currAge = age.iloc[i]
		if currDecade in freq:
			if currAge in freq[currDecade]:
				freq[currDecade][currAge] += 1
			else:
				key = {currAge: 1}
				freq[currDecade].update(key)
		else:
			key = {currDecade:{currAge: 1}}
			freq.update(key)

	#print(freq)
	file = open("MurderRateVicAgeDec.js", "w+")
	file.write(json.dumps(str(freq)))
	file.close()

################################

def murderVicAgeState():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	"""age = df['Victim Age']
	state = df['State']
	freq = dict()

	for i in range (0, len(df)):
		currState = state.iloc[i]
		currAge = age.iloc[i]
		if currState in freq:
			if currAge in freq[currState]:
				freq[currState][currAge] += 1
			else:
				key = {currAge: 1}
				freq[currState].update(key)
		else:
			key = {currState:{currAge:1}}
			freq.update(key)

	#print(freq)
	file = open("MurderVicAgeState.js", "w+")
	file.write(json.dumps(str(freq)))
	file.close()"""
	stat_counter = collections.Counter(df['Victim Age'])
	states_counter = collections.Counter(df['State'])
	output_dicts = [{'Victim Age': i, 'State': m, 'Frequency': f} for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("MurderVicAgeState.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()

################################

def cityWeapons():
	df = pd.ExcelFile('Murders.xlsx').parse('Sheet1')
	"""stateDf = df['State']
	cityDf = df['City']
	weaponDf = df['Weapon']
	data = dict()

	for x in range (0, len(df)):
		currState = stateDf.iloc[x]
		currCity = cityDf.iloc[x]
		currWeapon = weaponDf.iloc[x]
		if currState in data:
			if currCity in data[currState]:
				if currWeapon in data[currState][currCity]:
					data[currState][currCity][currWeapon] += 1
				else:
					s = {currWeapon: 1}
					data[currState][currCity].update(s)
			else:
				s = {currCity:{currWeapon:1}}
				data[currState].update(s)
		else:
			s = {currState:{currCity:{currWeapon:1}}}
			data.update(s)

	f = open("CityWeapons.js", "w+")
	f.write(json.dumps(data))
	f.close()"""
	st_counter = collections.Counter(df['State'])
        #stat_counter = collections.Counter(df['City'])
        #stat_counter = collections.Counter(df['City'])

	states_counter = collections.Counter(df['Weapon'])
	stat_counter = collections.Counter(df['City'])

	output_dicts = [{'State': s, 'City': i, 'Weapon': m, 'Frequency': f} for s, j in st_counter.items() for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("CityWeapons.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()


#################################PERPETRATOR SEX#############################

def perpSex():
	x1 = pd.ExcelFile('Murders.xlsx')
	df = x1.parse("Sheet1")
    
	# perpSexDict = dict()

	# allPerp = df["Perpetrator Sex"]
	# for key in allPerp:
	# 	if key in perpSexDict:
	# 		perpSexDict[key] += 1

	# 	else:
	# 		s = {key:1}
	# 		perpSexDict.update(s)
	#print(perpSexDict)

	freq1 = collections.Counter(df['Perpetrator Sex'])
	freq = [{'Perpetrator Sex': m, 'Freq': f} for m, f in freq1.items()]

	file = open("PerpSex.js", "w+")
	file.write(json.dumps(freq))
	file.close()

##############################PERPETRATOR RACE##############################

def perpRace():
	x1 = pd.ExcelFile('Murders.xlsx')
	df = x1.parse("Sheet1")
    
	# perpRaceDict = dict()

	# allPerp = df["Perpetrator Race"]
	# for key in allPerp:
	# 	if key in perpRaceDict:
	# 		perpRaceDict[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		perpRaceDict.update(s)
	#print(perpRaceDict)
	freq1 = collections.Counter(df['Perpetrator Race'])
	freq = [{'Perpetrator Race': m, 'Freq': f} for m, f in freq1.items()]

	file = open("PerpRace.js", "w+")
	file.write(json.dumps(freq))
	file.close()  


##############################VICTIM SEX##############################
    
def victSex():
	x1 = pd.ExcelFile('Murders.xlsx')
	df = x1.parse("Sheet1")
    
	# victSexDict = dict()

	# allVicts = df["Victim Sex"]
	# for key in allVicts:
	# 	if key in victSexDict:
	# 		victSexDict[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		victSexDict.update(s)
	#print(victSexDict)
	freq1 = collections.Counter(df['Victim Sex'])
	freq = [{'Victim Sex': m, 'Freq': f} for m, f in freq1.items()]

	file = open("VictSex.js", "w+")
	file.write(json.dumps(freq))
	file.close()  
   
##############################VICTIM RACE##############################

def victRace():
	x1 = pd.ExcelFile('Murders.xlsx')
	df = x1.parse("Sheet1")
    
	# victRaceDict = dict()

	# allVicts = df["Victim Race"]
	# for key in allVicts:
	# 	if key in victRaceDict:
	# 		victRaceDict[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		victRaceDict.update(s)
	#print(victRaceDict)

	freq1 = collections.Counter(df['Victim Race'])
	freq = [{'Victim Race': m, 'Freq': f} for m, f in freq1.items()]

	file = open("VictRace.js", "w+")
	file.write(json.dumps(freq))
	file.close()  

####################################AGENCY NAME IS EACH STATE########################

def stateAgen():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	"""yrDf = df['State']
	stateDf = df['Agency Name']
	yrStateDict = dict()

	for x in range (0, len(df)):
		currYear = yrDf.iloc[x]
		currState = stateDf.iloc[x]
		if currYear in yrStateDict:
			if currState in yrStateDict[currYear]:
				yrStateDict[currYear][currState] += 1
			else:
				s = {currState:1}
				yrStateDict[currYear].update(s)
		else:
			s = {currYear:{currState: 1}}
			yrStateDict.update(s)

	#print(yrStateDict)
	file = open("StateAgen.js", "w+")
	file.write(json.dumps(yrStateDict))
	file.close()  """
	stat_counter = collections.Counter(df['State'])
	states_counter = collections.Counter(df['Agency Name'])
	output_dicts = [{'State': i, 'Agency Name': m, 'Frequency': f} for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("StateAgen.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()




###############################Weapon Used Based on Perpetrator Sex########################################

def weaponPerpSex():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	"""yrDf = df['Weapon']
	stateDf = df['Perpetrator Sex']
	yrStateDict = dict()

	for x in range (0, len(df)):
		currYear = yrDf.iloc[x]
		currState = stateDf.iloc[x]
		if currYear in yrStateDict:
			if currState in yrStateDict[currYear]:
				yrStateDict[currYear][currState] += 1
			else:
				s = {currState:1}
				yrStateDict[currYear].update(s)
		else:
			s = {currYear:{currState: 1}}
			yrStateDict.update(s)

	# print(yrStateDict)
	# print(counts)
	file = open("WeaponPerpSex.js", "w+")
	file.write(json.dumps(yrStateDict))
	file.close()  """
	stat_counter = collections.Counter(df['Weapon'])
	states_counter = collections.Counter(df['Perpetrator Sex'])
	output_dicts = [{'Weapon': i, 'Perpetrator Sex': m, 'Frequency': f} for i, r in stat_counter.items() for m, f in states_counter.items()]
	file = open("WeaponPerpSex.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()



#######################################How many crimes happen per month##################################################

def crimesMonth():
	x1 = pd.ExcelFile('Murders.xlsx')
	df = x1.parse("Sheet1")
	# monthDict = dict()
	# allMonth = df["Month"]

	# for key in allMonth:
	# 	if key in monthDict:
	# 		monthDict[key] += 1
	# 	else:
	# 		s = {key:1}
	# 		monthDict.update(s)
	# print(monthDict)
	# file = open("CrimesMonth.js", "w+")
	# file.write(json.dumps(monthDict))
	# file.close()
	month_counter = collections.Counter(df['Month'])

	output_dicts = [{'Month': m, 'Freq': f} for m, f in month_counter.items()]
	#print(json.dumps(output_dicts))
	file = open("CrimesMonth.js", "w+")
	file.write(json.dumps(output_dicts))
	file.close()

######################################################################################################

#murderRateState()
# murderRateDecState()
#weaponRelationship()
#raceWeapon()
#murderPerpAge()
# murderRatePerpAgeDec()
#murderPerpAgeState()
#murderVicAge()
# murderRateVicAgeDec()
#murderVicAgeState()
# cityWeapons() # file too big 
#perpSex()
#perpRace()
#victSex()
#victRace()
# stateAgen() # too big file
# weaponPerpSex() # too big file
#crimesMonth()
