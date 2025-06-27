# In this file we explore some of the basic libraries in Python

### BUILT-IN FUNCTIONS ###

message = "Hello, nice to meet you"
numbers = [4, 3, 5, 1, 2]

# measures the length of a variable
length = len(message)

# sums elements of a list
sum = sum(numbers)

# organizes a list (by ascending order)
sorted_numbers = sorted(numbers)

import os # operating system interfaces

song = """
We keep this love in a photograph
We made these memories for ourselves
Where our eyes are never closing
Our hearts were never broken
And time's forever frozen still
""" # a part of the song 'Photograph' by Ed Sheeran

# split a string in lines
lines = song.split(os.linesep)
print(lines)

# Pandas - data analysis
# ### Serie = 'column'
# ### DataFrame = 'table'

import pandas as pd

# Creating a DataFrame from a dictionary

patients_1 = {'Name': ['Tom', 'Ana', 'Bob', 'Mary'],
             'Age': [23, 36, 48, 56],
             'Diagnostic': ['Diabetes', 'Diabetes', 'Hypertension', 'Hypertension']}

patients_2 = {'Name': ['Joseph', 'Claire', 'Evelyn', 'Don'],
             'Age': [73, 29, 37, 48],
             'Diagnostic': ['Hypothyroidism', 'Hypothyroidism', 'Diabetes', 'Hypertension']}

df_patients_1 = pd.DataFrame(patients_1)

df_patients_2 = pd.DataFrame(patients_2)

# Merging the 2 data frames

df_all_patients = pd.concat([df_patients_1, df_patients_2],
                            ignore_index=True) # gives a new index sequence to the new dataframe

print(df_all_patients)

# Sorting the dataframe by a column

df_all_patients = df_all_patients.sort_values(by="Name", ascending=True)
print(df_all_patients)

# List of diagnostics

diagnostics = df_all_patients['Diagnostic'].unique()
print(diagnostics)

# Export a dataframe to a .csv format

df_all_patients.to_csv('df_example.csv', sep='\t')

# Import a .csv as a dataframe

df_imported = pd.read_csv('df_example.csv', sep='\t')
print(df_imported)