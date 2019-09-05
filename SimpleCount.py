import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Select the excel file to work with.
officer = input('Officer Last Name, First Name: ')
csv_file = input('Name of file with extension: ')

# Read the entire file first argument is sheetname then index_col
activity = pd.read_csv(csv_file)

# Create a dataframe in Panda
df = pd.DataFrame(activity)

officer_filter_df = df[df['OfficerName_1']== officer] 

total_time_officer_df = officer_filter_df[['TotalTime']].sum()
total_activities_officer_df = officer_filter_df[['InitialIncidentOffenceCode']].count()


# The .values[0] function just returns the value with no index.
print ('Total Minutes:', total_time_officer_df.values[0])
print ('Total Walkthroughs:', total_activities_officer_df.values[0])











# Pulls all the data from one Column.
# print (df['Date'])

# Pulls all the data from multiple Columns.
# print (df[['Date', 'Officer', 'Total Time']])