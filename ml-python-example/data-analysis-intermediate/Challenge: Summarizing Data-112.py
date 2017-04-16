## 2. Introduction to the Data ##

import pandas as pd
all_ages=pd.read_csv('all-ages.csv')
recent_grads= pd.read_csv('recent-grads.csv')
print(all_ages.head(5))
print(recent_grads.loc[0:5])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()
for major_category in recent_grads['Major_category'].unique():
    category_all = recent_grads[recent_grads['Major_category']==major_category]
    total = category_all['Total'].sum()
    rg_cat_counts[major_category] = total
    
for major_category in all_ages['Major_category'].unique():
    category_all = all_ages[all_ages['Major_category']==major_category]
    total = category_all['Total'].sum()
    aa_cat_counts[major_category] = total

print(aa_cat_counts)

          

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage = recent_grads['Low_wage_jobs'].sum()
total_student=recent_grads['Total'].sum()
low_wage_percent=low_wage/total_student
print(low_wage_percent)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for major in majors:
    major_age=all_ages[all_ages['Major']==major]
    age_unempolyment=major_age['Unemployment_rate']
    major_age=recent_grads[recent_grads['Major']==major]
    rgrads_unempolyment=major_age['Unemployment_rate']
    if rgrads_unempolyment.sum()<age_unempolyment.sum():
        rg_lower_count +=1
print(rg_lower_count)
    
    