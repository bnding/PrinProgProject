import pandas as pd

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

	#ONE METHOD
	#counts = df.groupby(['State', 'Decade']).count()
	#counts = counts.reset_index()[['State', 'Decade','Victim Count']]

	#ANOTHER METHOD
	counts = df.loc[:,['State', 'Decade','Victim Count']].groupby(['State', 'Decade']).count()

	print(counts)


################################

def weaponRelationship():
	xl = pd.ExcelFile('Wyoming.xlsx')
	df = xl.parse('Sheet1')

	#ONE METHOD
	# counts = df.groupby(['Weapon', 'Relationship']).count()
	# counts = counts.reset_index()[['Weapon', 'Relationship','Victim Count']]

	#ANOTHER METHOD
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

#murderRateDec()
#yearMurders()
weaponRelationship()