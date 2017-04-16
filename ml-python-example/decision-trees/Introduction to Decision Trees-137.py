## 3. Converting Categorical Variables ##

# Convert a single column from text categories to numbers
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))

catg_features= ['education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'high_income']

for feature in catg_features:
    col = pandas.Categorical.from_array(income[feature])
    income[feature]=col.codes


## 5. Creating Splits ##

private_incomes = income[income['workclass']==4]
public_incomes = income[income['workclass']!=4]

## 8. Overview of Data Set Entropy ##

import math
import numpy as np
from scipy.stats import entropy as fn_entropy



# We'll do the same calculation we did above, but in Python
# Passing in 2 as the second parameter to math.log will take a base 2 log
entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
print(entropy)

# Input a pandas series 
def entropy_func(data):
    p_data= data.value_counts()/len(data) # calculates the probabilities
    entropy=fn_entropy(p_data)  # input probabilities to get the entropy 
    return entropy

counts = np.bincount(income['high_income'])
probs = counts / len(income['high_income'])
n_classes = np.count_nonzero(probs)
income_entropy =0.
if n_classes >= 1:
    income_entropy =- np.sum(probs * np.log2(probs))

print(income_entropy)

## 9. Information Gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)
income_entropy = calc_entropy(income["high_income"])

median_age = income["age"].median()

left_split = income[income["age"] <= median_age]
right_split = income[income["age"] > median_age]

age_information_gain = income_entropy - ((left_split.shape[0] / income.shape[0]) * calc_entropy(left_split["high_income"]) + ((right_split.shape[0] / income.shape[0]) * calc_entropy(right_split["high_income"])))

## 10. Finding the Best Split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data, based on the median
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain
    return original_entropy - to_subtract

# Verify that our answer is the same as on the last screen
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

max_gain =0.
highest_gain=''
information_gains=[]
for column in columns:
    gain = calc_information_gain(income, column, "high_income")
    if gain>max_gain:
        max_gain = gain
        highest_gain = column
    information_gains.append(gain)
print(highest_gain)