## 2. Introduction to the Data Set ##

import pandas as pd
train = pd.read_csv('train.csv')
columns_name=["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
titanic = train[columns_name]
titanic = titanic.dropna()

## 3. Creating Histograms In Seaborn ##

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(titanic['Age'])
plt.show()

## 4. Generating A Kernel Density Plot ##

import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(titanic["Age"],shade=True)
plt.xlabel("Age")
plt.show()

## 5. Modifying The Appearance Of The Plots ##

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("white")
sns.kdeplot(titanic['Age'],shade=True)
sns.despine(left=True,top=True,bottom=True)
plt.xlabel('Age')
plt.show()

## 6. Conditional Distributions Using A Single Condition ##

import seaborn as sns
import matplotlib.pyplot as plt
g=sns.FacetGrid(titanic,col='Pclass',size=6)
g.map(sns.kdeplot,"Age",shade=True)
sns.despine(left=True,bottom=True,top=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex",size=3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

import seaborn as sns
import matplotlib.pyplot as plt
g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex",size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()
