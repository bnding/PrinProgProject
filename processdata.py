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
#################################PERPETRATOR SEX#############################

def perpSex():
    x1 = pd.ExcelFile('SmallSample.xlsx')
    df = x1.parse("Sheet1")
    
    perpSexDict = dict()

    allPerp = df["Perpetrator Sex"]
    for key in allPerp:
        if key in perpSexDict:
            perpSexDict[key] += 1

        else:
            s = {key:1}
            perpSexDict.update(s)
    print(perpSexDict)
        


##############################PERPETRATOR RACE##############################

def perpRace():
    x1 = pd.ExcelFile('SmallSample.xlsx')
    df = x1.parse("Sheet1")
    
    perpRaceDict = dict()

    allPerp = df["Perpetrator Race"]
    for key in allPerp:
        if key in perpRaceDict:
            perpRaceDict[key] += 1

        else:
            s = {key:1}
            perpRaceDict.update(s)
    print(perpRaceDict)
        


##############################VICTIM SEX##############################
    
def victSex():
    x1 = pd.ExcelFile('SmallSample.xlsx')
    df = x1.parse("Sheet1")
    
    victSexDict = dict()

    allVicts = df["Victim Sex"]
    for key in allVicts:
        if key in victSexDict:
            victSexDict[key] += 1

        else:
            s = {key:1}
            victSexDict.update(s)
    print(victSexDict)

   
##############################VICTIM RACE##############################

def victRace():
    x1 = pd.ExcelFile('SmallSample.xlsx')
    df = x1.parse("Sheet1")
    
    victRaceDict = dict()

    allVicts = df["Victim Race"]
    for key in allVicts:
        if key in victRaceDict:
            victRaceDict[key] += 1

        else:
            s = {key:1}
            victRaceDict.update(s)
    print(victRaceDict)

####################################AGENCY NAME IS EACH STATE########################

def stateAgen():
	xl = pd.ExcelFile('SmallSample.xlsx')
	df = xl.parse('Sheet1')
	yrDf = df['State']
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

	print(yrStateDict)


#########################################Weapon Used Based on Perpetrator Sex############################################

def weaponPerpSex():
	xl = pd.ExcelFile('SmallSample.xlsx')
	df = xl.parse('Sheet1')

	#ONE METHOD
	# counts = df.groupby(['Weapon', 'Relationship']).count()
	# counts = counts.reset_index()[['Weapon', 'Relationship','Victim Count']]

	#ANOTHER METHOD
	counts = df.loc[:,['Weapon', 'Perpetrator Sex','Record ID']].groupby(['Weapon', 'Perpetrator Sex']).count()
	print(counts)


#######################################How many crimes happen per month#################################################################


def crimesMonth():
    x1 = pd.ExcelFile('SmallSample.xlsx')
    df = x1.parse("Sheet1")
    
    monthDict = dict()

    allMonth = df["Month"]
    for key in allMonth:
        if key in monthDict:
            monthDict[key] += 1

        else:
            s = {key:1}
            monthDict.update(s)
    print(monthDict)

######################################################################################################

