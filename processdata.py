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
	decDict = dict()


	currDec = df['Year'][0]
	# yearCount = 0

	entries = df[['State', 'Year']]

	entries = entries.sort_values(by='Year', ascending=True)
	# print(entries)

	allStates = entries['State']
	years = entries['Year']

	for year in years:
		if year - currDec < 10:
			for key in #TODO: Need to find a way to get states in the current decade:
				if key in currDecDict:
					decDict[key] += 1
				else:
					s = {key:1}
					currDecDict.update(s)
			decDict.update({currDec : currDecDict})
		else: 
			currDec = year

	print(decDict)

murderRateDec()
