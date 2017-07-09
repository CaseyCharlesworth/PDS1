# s3132392 Casey-Ann Charlesworth
# Part 1 of Assignment 1 - Practical Data Science
# Assignment due 30 March 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# function to mask
def masking(variable, incorrect, correct):
    mask = ratings[variable] == incorrect
    ratings.loc[mask, variable] = correct


# import file (Q1 & Q2)
filename = "TeachingRatings.csv"
ratings = pd.read_csv(filename, sep=",", decimal=".", header=0)
ratings["prof"] = ratings["prof"].astype(str)  # changed as variable is not for calculations

# fix typos with masks (Q3)
variable = ['minority', 'native', 'tenure']
yesses = ["yesd", "yer", "yed"]
nos = ["noo", "N0"]

for v in variable:
    for n in nos:
        masking(v, n, "no")
    for y in yesses:
        masking(v, y, "yes")

# gender - not required as only upper case issues

# credits
creds = ["mOre", "much more"]

for cr in creds:
    masking("credits", cr, "more")

# division
masking("division", "lowered", "lower")

# strip whitespace and cast text data to lower (Q4 & Q5)
string_variables = ratings.loc[:, ratings.dtypes == object]
for v in string_variables:
    ratings[v] = ratings[v].str.lower()
    ratings[v] = ratings[v].str.strip()

# fix impossible values (Q6)
# age (replace <0 and >100 with NaN values to be replaced with column-wise mean later)
# Sanity check below - will be commented out for submission
# bad_lines = ratings.loc[(ratings["age"] < 0) | (ratings["age"] > 100)]
# print(bad_lines)
maskv = (ratings["age"] < 0) | (ratings["age"] > 100)
ratings.loc[maskv, "age"] = np.nan

# eval
# Sanity check below - will be commented out for submission
# bad_lines = ratings.loc[(ratings["eval"] < 1) | (ratings["eval"] > 5)]
# print(bad_lines)
maskv = (ratings["eval"] < 1) | (ratings["eval"] > 5)
ratings.loc[maskv, "eval"] = np.nan

# students and all students
# Sanity check below - will be commented out for submission
# bad_lines = ratings.loc[ratings["students"] > ratings["allstudents"]]
# print(bad_lines)
maskv = (ratings["students"] > ratings["allstudents"])
ratings.loc[maskv, "students"] = ratings["allstudents"] * 2 / 3
ratings["students"] = ratings["students"].astype(int)  # calc in above line forced type to float - returned to int

# Replace NaNs with column-wise mean (Q7)
ratings.fillna(ratings.mean(axis=0), inplace=True)

# Finally, convert "age" to int (part of (Q1))
ratings["age"] = ratings["age"].astype(int)

print("Data preprocessing step complete")
