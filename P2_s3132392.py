#s3132392 Casey-Ann Charlesworth
#Part 2 of Assignment 1 - Practical Data Science
#Assignment due 30 March 2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import P1_s3132392 as p1

#(Q1) - Single category charts
p1.ratings["minority"].value_counts().plot(kind="pie",autopct="%.2f",title="Teacher Ratings - minority count by percentage")
plt.show()
p1.ratings["minority"].value_counts().plot(kind="bar",title="Teacher Ratings - minority totals")
plt.xlabel("Minority")
plt.ylabel("Totals")
plt.show()
p1.ratings["age"].plot(kind="hist",bins=10, edgecolor="white", linewidth=1.0)
plt.title("Teacher Ratings - age distribution")
plt.xlabel("Age")
plt.show()
p1.ratings["age"].plot(kind="box")
plt.title("Teacher Ratings - boxplot of age")
plt.show()
p1.ratings["gender"].value_counts().plot(kind="pie",autopct="%.2f")
plt.title("Teacher Ratings - gender count by percentage")
plt.show()
p1.ratings["credits"].value_counts().plot(kind="bar",title="Teacher Ratings - credits totals")
plt.xlabel("Credits")
plt.ylabel("Totals")
plt.show()
p1.ratings["beauty"].plot(kind="density")
plt.title("Teacher Ratings - density of beauty")
plt.show()
p1.ratings["eval"].plot(kind="hist",bins=10,edgecolor="white",linewidth=1.0)
plt.title("Teacher Ratings - eval distribution")
plt.xlabel("Evaluation")
plt.show()
p1.ratings["division"].value_counts().plot(kind="pie",autopct="%.2f")
plt.title("Teacher Ratings - division count by percentage")
plt.show()
p1.ratings["native"].value_counts().plot(kind="pie",autopct="%.2f")
plt.title("Teacher Ratings - native count by percentage")
plt.show()
p1.ratings["tenure"].value_counts().plot(kind="bar")
plt.title("Teacher Ratings - tenure totals")
plt.xlabel("Credits")
plt.ylabel("Totals")
plt.show()
p1.ratings["students"].plot(kind="box")
plt.title("Teacher Ratings - boxplot of students")
plt.show()
p1.ratings["allstudents"].plot(kind="density")
plt.title("Teacher Ratings - density of all students")
plt.show()

#(Q2) - multi category charts
#(Q2.1 - eval vs beauty)
p1.ratings.plot(kind="scatter", x="eval", y="beauty")
plt.title("Teacher Ratings - scatter plot of eval vs beauty")
plt.show()

#(Q2.2 - beauty by gender)
p1.ratings.boxplot(column="beauty", by="gender")
plt.show()

#(Q2.3 - age and eval)
p1.ratings.plot(kind="hexbin", x="age", y="eval", gridsize=10)
plt.title("Teacher Ratings - scatter plot of age vs evaluation")
plt.show()

#(Q3) - Scatter matrix
from pandas.tools.plotting import scatter_matrix
vars=["age","beauty","eval","students","allstudents"]
scatter_matrix(p1.ratings[vars],alpha=0.3,diagonal="density")
plt.suptitle("Teacher Ratings - scatter matrix of numerical data")
plt.show()
