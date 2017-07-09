#s3132392 Casey-Ann Charlesworth
#Part 3C of Assignment 1 - Practical Data Science
#Assignment due 30 March 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#function to mask
def masking(variable, incorrect, correct):
    mask = ratings[variable] == incorrect
    ratings.loc[mask, variable] = correct

#import file (Q1 & Q2)
filename = "TeachingRatings.csv"
ratings = pd.read_csv(filename,sep=",", decimal=".", header=0)
ratings["prof"] = ratings["prof"].astype(str) #changed as variable is not for calculations


#fix typos with masks (Q3)
variable = ['minority', 'native', 'tenure']
yesses = ["yesd", "yer", "yed"]
nos = ["noo", "N0"]

for v in variable:
    for n in nos:
        masking(v, n, "no")
    for y in yesses:
        masking(v, y, "yes")

#gender - not required as only upper case issues

#credits
creds = ["mOre", "much more"]

for cr in creds:
    masking("credits", cr, "more")

#division
masking("division", "lowered", "lower")

#strip whitespace and cast text data to lower (Q4 & Q5)
string_variables = ratings.loc[:, ratings.dtypes == object]
for v in string_variables:
    ratings[v] = ratings[v].str.lower()
    ratings[v] = ratings[v].str.strip()

#fix impossible values (Q6)
#age 
maskv = (ratings["age"] < 0) | (ratings["age"] > 100)
ratings.loc[maskv, "age"] = np.nan

#eval 
maskv = (ratings["eval"] < 1) | (ratings["eval"] > 5)
ratings.loc[maskv, "eval"] = np.nan

#students and all students
maskv = (ratings["students"] > ratings["allstudents"])
ratings.loc[maskv, "students"] = ratings["allstudents"]*2/3
ratings["students"] = ratings["students"].astype(int) #calc in above line forced type to float - returned to int

#Replace NaNs with nothing (graph will be created to ignore these rows)

#Finally, convert "age" to int (part of (Q1))
#Unable to convert "age" to int due to NaNs still present
#ratings["age"] = ratings["age"].astype(int)

print("Data preprocessing step (3C) complete")

#create new graph
ratings["age"].dropna().plot(kind="hist",bins=10, edgecolor="white", linewidth=1.0)
plt.title("Teacher Ratings - age distribution")
plt.xlabel("Age")
plt.show()
ratings["age"].dropna().plot(kind="box")
plt.title("Teacher Ratings - boxplot of age")
plt.show()

