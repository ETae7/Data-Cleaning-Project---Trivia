import pandas as pd

#Import from /Users... file location
df = pd.read_csv("Trivia.csv")

#Changing "Correct" column >> String to Int >> as Values for "Question"
df.loc[df['Correct'] == 'Y', 'Correct'] = '1'
df.loc[df['Correct'] == 'N', 'Correct'] = '0'
df['Correct'] = df['Correct'].astype(int)
df['Correct'] = df['Correct'].fillna(0)

#Pivot Table + Reset index
df = df.pivot_table(index=['Time', 'Topic', 'Location', 'Measure', 'CustomerID', 'DateReported', 'PossiblePoints'], columns = 'Question', values = 'Correct')
df = df.reset_index()

#Filling NA Values
df = df.fillna(0)

#Calculate Raw Score    
df['RawScore'] = df[df.columns[7]]
for x in range(8, 27):
    df['RawScore'] = df['RawScore'] + df[df.columns[x]]
    
#Calculate Percent Score
df['PercentScore'] = (df['RawScore']/df['PossiblePoints'])*100

#to excel
df.to_csv('Trivia_Finished.csv')