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
