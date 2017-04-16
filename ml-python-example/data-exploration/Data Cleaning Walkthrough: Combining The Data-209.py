## 2. Condensing class size ##

class_size = data['class_size']
class_size = class_size[class_size['GRADE ']=='09-12']
class_size  = class_size[class_size['PROGRAM TYPE']=='GEN ED']
print(class_size.head(5))

## 3. Computing average class sizes ##

import numpy as np
grouped =  class_size.groupby('DBN')
class_size = grouped.aggregate(np.mean)
class_size.reset_index(inplace=True)
data['class_size'] = class_size
print(data['class_size'].head(5))

## 4. Condensing demographics ##

import pandas as pd
demographics = data["demographics"]
demographics = demographics[demographics['schoolyear']== int(20112012)]
data["demographics"] = demographics
demographics.head()

## 5. Condensing graduation ##

import pandas as pd
graduation  = data["graduation"]
graduation  = graduation[graduation['Cohort']== '2006']
graduation  = graduation[graduation['Demographic']== 'Total Cohort']

data["graduation"] = graduation
graduation.head()

## 6. Converting AP test scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col],errors="coerce")
data['ap_2010'].head()
                 

## 8. Performing the left joins ##

combined = data["sat_results"]
combined = combined.merge(data['ap_2010'],on='DBN',how='left')
combined = combined.merge(data['graduation'],on='DBN',how='left')
print(combined.head())
print(combined.shape)

## 9. Performing the inner joins ##

combined = combined.merge(data['class_size'],on='DBN',how='inner')
combined = combined.merge(data['demographics'],on='DBN',how='inner')
combined = combined.merge(data['survey'],on='DBN',how='inner')
combined = combined.merge(data['hs_directory'],on='DBN',how='inner')
print(combined.head())
print(combined.shape)

## 10. Filling in missing values ##

means = combined.mean()
combined = combined.fillna(means)
combined = combined.fillna(0)
combined.loc[0:1]

## 11. Adding a school district column ##

def distName(dbn):
    return dbn[0:2]
combined['school_dist']=combined['DBN'].apply(distName)
print(combined['school_dist'].head(5))