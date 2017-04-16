## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt
admissions=pd.read_csv('admissions.csv')
#admissions.plot('gpa','admit',kind='scatter')
plt.scatter(admissions['gpa'],admissions['admit'])
plt.show()

## 4. Logit function ##

import numpy as np

# Logit Function
def logit(x):
    # np.exp(x) raises x to the exponential power, ie e^x. e ~= 2.71828
    return np.exp(x)  / (1 + np.exp(x)) 
    
# Generate 50 real values, evenly spaced, between -6 and 6.
x = np.linspace(-6,8,45, dtype=float)

# Transform each number in t using the logit function.
y = logit(x)

# Plot the resulting data.
plt.plot(x, y)
plt.ylabel("Probability")
plt.show()

## 5. Training a logistic regression model ##

import numpy as np

# Logit Function
def logit(x):
    # np.exp(x) raises x to the exponential power, ie e^x. e ~= 2.71828
    return np.exp(x)  / (1 + np.exp(x)) 
    
# Generate 50 real values, evenly spaced, between -6 and 6.
x = np.linspace(-6,8,45, dtype=float)

# Transform each number in t using the logit function.
y = logit(x)

# Plot the resulting data.
plt.plot(x, y)
plt.ylabel("Probability")
plt.show()

## 6. Plotting probabilities ##

import matplotlib.pyplot as plt
logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
pred_probs = logistic_model.predict_proba(admissions[["gpa"]])
# Probability that the row belongs to label `0`.
#pred_probs[:,0]
# Probabililty that the row belongs to label `1`.
label_one=pred_probs[:,1]
plt.scatter(admissions['gpa'],label_one)
plt.show()

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
fitted_labels = logistic_model.predict(admissions[['gpa']])
print(fitted_labels[0:10])