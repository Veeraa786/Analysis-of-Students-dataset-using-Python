import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

# merge those two csv files (after getting as dataframes, get them as a single dataframe)
data1 = pd.read_csv("C:\\Users\\Intel\\PycharmProjects\\Myfirstproject\\college_1.csv")
data2 = pd.read_csv("C:\\Users\\Intel\\PycharmProjects\\Myfirstproject\\college_2.csv")
df = pd.concat([data1,data2])

# consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
exceed = df[(df["CodeKata_Score"]>15000)]
exceed.to_csv("Exceed_Expectations.csv",index = False)

# if 10000<codekata score<15000 (Reached_expectations.csv)
reached = df[(df["CodeKata_Score"].between(10000,15000))]
reached.to_csv("Reached_Expectations.csv",index = False)

# if 7000<codekata score<10000 (Needs_Improvement.csv)
needs = df[(df["CodeKata_Score"].between(7000,10000))]
needs.to_csv("Needs_Improvement.csv",index=False)

# if codekate score < 7000 (Unsatisfactory.csv)
unsatisfy = df[(df["CodeKata_Score"]<7000)]
unsatisfy.to_csv("Unsatisfactory.csv",index = False)

# Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)
df["Average"] = (df["Previous_Geekions"]+df["CodeKata_Score"])/2

# No of students participated
no_of_students = df['Name'].count()

#Average completion of python course or my_sql or python english or computational thinking
average_python = (df["python"].sum())/no_of_students

# rising star of the week (top 3 candidate who performed well in that particular week)
rising_star = df.nlargest(3,["Rising"])
rising_star.to_csv('top_3_rising.csv',index=False)

# Shining stars of the week (top 3 candidates who has highest geekions)
greek = df.nlargest(3,["Previous_Geekions"])
greek.to_csv('top_3_shing.csv',index=False)

# Department wise codekata performence (pie chart)
comp = df[(df["Department"] == 'Computer Science and Engineering')]
computer_total = comp["CodeKata_Score"].sum()
elec = df[(df["Department"] == 'Electronics and Communication Engineering')]
ece_total = elec["CodeKata_Score"].sum()
elec_eng = df[(df["Department"] == 'Electronics and Electrical Engineering')]
eee_total = elec_eng["CodeKata_Score"].sum()
data = [computer_total,ece_total,eee_total]
fig = plt.figure(figsize=(10,7))
plt.pie(data,labels = ['Computer Science and Engineering','Electronics and Communication Engineering','Electronics and Electrical Engineering'])
plt.show()
print()

