# In this file we explore some of the basic libraries in Python

import os

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

patients = {'Name': ['Tom', 'Ana', 'Bob', 'Mary'],
             'Age': [23, 36, 48, 56],
             'Diagnostic': ['Diabetes', 'Diabetes', 'Hypertension', 'Hypertension']}

df_patients = pd.DataFrame(patients)
print(df_patients)
