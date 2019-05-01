import pandas as pd
import json

################################
def murderRateState():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse("Sheet1")
	statesDict = dict()

	allStates = df["State"]
	for key in allStates:
		if key in statesDict:
			statesDict[key] += 1
		else:
			s = {key:1}
			statesDict.update(s)

	print(statesDict)

################################

def murderRateDec():
	xl = pd.ExcelFile('Wyoming.xlsx')
	df = xl.parse('Sheet1')
	
	df['Decade'] = (df['Year'] // 10) * 10

	counts = df.loc[:,['State', 'Decade','Victim Count']].groupby(['State', 'Decade']).count()

	print(counts)

################################

def weaponRelationship():
	xl = pd.ExcelFile('Wyoming.xlsx')
	df = xl.parse('Sheet1')

	counts = df.loc[:,['Weapon', 'Relationship','Victim Count']].groupby(['Weapon', 'Relationship']).count()
	print(counts)


################################

def yearMurders():
	xl = pd.ExcelFile('Murders.xlsx')
	df = xl.parse('Sheet1')
	yrDf = df['Year']
	stateDf = df['State']
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

	print(yrStateDict)

################################

def cityWeapons():
	df = pd.ExcelFile('Murders.xlsx').parse('Sheet1')
	stateDf = df['State']
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
					data[currState][currCity][currWeapon] += 1;
				else:
					s = {currWeapon: 1}
					data[currState][currCity].update(s)
			else:
				s = {currCity:{currWeapon:1}}
				data[currState].update(s)
		else:
			s = {currState:{currCity:{currWeapon:1}}}
			data.update(s)

	f = open("CityWeapons.txt", "w+")
	f.write(json.dumps(data))
	f.close()

	print("done writing file\n")



# murderRateDec()
cityWeapons()
#yearMurders()
# weaponRelationship()

#####################

