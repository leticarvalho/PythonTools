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

# Sorting the dataframe by a column

df_all_patients = df_all_patients.sort_values(by="Name", ascending=True)


# List of diagnostics

diagnostics = df_all_patients['Diagnostic'].unique()


# Export a dataframe to a .csv format

df_all_patients.to_csv('df_example.csv', sep='\t')

# Import a .csv as a dataframe

df_imported = pd.read_csv('df_example.csv', sep='\t')


# Peek at the data of a dataframe
df_imported.head(3) # show the first 3 rows
df_imported.tail(2) # show the last 2 rows


# Understanding the structure of a dataframe
df_imported.columns # show columns names
df_imported.shape # show how many rows x columns
#df_imported.info() # summary with datatypes and non-null values


# Selecting specific data
df_all_patients['Name'] # selecting only the column of Names
diagnostic_2 = df_all_patients.loc[7,'Diagnostic'] # selecting a row and a column
df_2 = df_all_patients.set_index('Name') # setting a column as row index
print(df_2.loc['Don', 'Diagnostic'] == diagnostic_2)


# Describing summary statistics (of numeric variables)
# useful for gene expression distributions
print(df_all_patients.describe())