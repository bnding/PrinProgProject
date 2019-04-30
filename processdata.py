import pandas as pd

################################
def murderRateState():
	xl = pd.ExcelFile('Wyoming.xlsx')
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

#scrapping this for now
# def murderRateDec():
# 	xl = pd.ExcelFile('Wyoming.xlsx')
# 	df = xl.parse('Sheet1')
# 	decDict = dict()
# 	currDecDict = dict()

# 	currDec = df['Year'][0]
# 	# yearCount = 0

# 	entries = df[['Year', 'State']]
# 	stateYear = df[['State', 'Year']]
# 	#print(entries['Year'])
# 	entries = entries.sort_values(by='Year', ascending=True)
# 	print(entries)

# 	allStates = entries['State']
# 	years = entries['Year']

# 	df.groupby([df['Year'].dt.year.rename('year'), df['State'].dt.state.rename('state')]).agg({'count'})
# 	print(df)
# 	statesYear = {}
# 	key = None
# 	for item in SOMETHINGHERE:
# 		if key is None:
# 			key = item
# 		else:
# 			if key not in statesYear:
# 				statesYear[key] = []
# 			statesYear[key].append(item)
# 			key = None
# 	print(statesYear)
# #TODO: Need to find a way to get states in the current decade:
# 	for year in years:
# 		if year - currDec < 10:
# 			for key in statesYear[year]:
# 				if key in currDecDict:
# 					decDict[key] += 1
# 				else:
# 					s = {key:1}
# 					currDecDict.update(s)
# 			decDict.update({currDec : currDecDict})
# 		else: 
# 			currDec = year

# 	print(decDict)

# murderRateState()
yearMurders()
# murderRateDec()