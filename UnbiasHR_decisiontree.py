from sklearn.tree import DecisionTreeClassifier
import numpy as np

#Model receives inputs based on candidate's experience, education, interview scores, gender 
#Scores for each one based on 0-1 
#Based on previous result asks more questions 
#If female - model create identical candidate with identical answers except for gender 

# how do to if else with basic inputs like education, where does it break off into more specific 
#this or random tree or what? 

#education = input("How many years of education do you have?: ")

#education_train_years = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
#education_number = np.array([0, 0, 0, 1, 1, 1])

#model = DecisionTreeClassifier()
#model.fit(education_train_years, education_number)

#predictions = model.predict[[]]
#print(predictions[0])

#HIRING MODEL 

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()




#Male = 0
#Female = 1


df = pd.read_csv("data.csv")

feature_columns = df.columns.drop("hired")

X_train = df[feature_columns]
y_train = df["hired"]

model.fit(X_train, y_train)

candidate = [[8,92,0,4,95]]

#ADD INPUT HERE AND CHANGE DATA 
prediction = model.predict(candidate)



probability = model.predict_proba(candidate)
for cls, prob in zip(model.classes_, probability[0]):
    if cls == 0:
        print(f"Chances of NOT being Hired: {prob: .2%}")
    else:
        print(f"Chances of being Hired: {prob: .2%}")

print(f'Chance of getting hired (0 is none, 1 is hired): {prediction}') # Chance of getting hired 1 and 0

print("\n --- Feature Importance --- ")
for feature, importance in zip(X_train.columns, model.feature_importances_):
    print(f"{feature}: {importance: .1%}")

#data = {
#    "experience": [8,2,10,4,7,1,9,3,6,3], 
#    "interview_score": [90,60,95,60,85,30,88,55,40,20],
#    "hired": [1,0,1,0,1,0,1,0,1,0],
#    "gender": [0,1,0,0,1,0,1,0,0,0]
#    }

# DISPARATE IMPACT RATIO 
female_applicants = len(df[df["gender"] == 1])
male_applicants = len(df[df["gender"] == 0])
import matplotlib.pyplot as plt

#Scatter Plot - Relation between experience and hiring 

#plt.scatter(df['experience'], df['hired'])
#plt.xlabel("Experience")
#plt.ylabel("Hired")
#plt.show()


# Double Bar Chart - Relation between gender and hired 

#pd.crosstab(df['gender'], df['hired']).plot(
#    kind = 'bar', 
#    stacked = False
#)
#plt.xlabel('Gender')
#plt.ylabel('Count')
#plt.title("Hiring Count Based on Gender")
#plt.show()



female_hires = len(df[(df["hired"] == 1) & (df["gender"]== 1)])
male_hires = len(df[(df["hired"] == 1) & (df["gender"] == 0)])

selection_rate_female = female_hires/female_applicants
selection_rate_male = male_hires/male_applicants

print(f"Selection Rate Female: {selection_rate_female: .1%}")
print(f"Selection Rate Male: {selection_rate_male: .1%}")

disparate_impact_ratio = (
    min(selection_rate_female,selection_rate_male) / 
    max(selection_rate_female,selection_rate_male)
)

print(f"Impact Ratio {disparate_impact_ratio}")

if disparate_impact_ratio < 0.80:
   risk = True 
   print("Potential disparate impact detected")
else:
   risk= False 
   print("No disparate impact detected")



#1 = hired 
#0 = not hired 


