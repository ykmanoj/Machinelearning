## 4. Reading in the data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for files in data_files:
    file_name= files.split('.')[0]
    data[file_name]=pd.read_csv('schools/'+files)
print(data.keys())

## 5. Exploring the SAT data ##

sat_resuts= data['sat_results']
print(sat_resuts.head(5))

## 6. Exploring the other data ##

for key in data:
    print(data[key].head(5))

## 7. Reading in the survey data ##

all_survey = pd.read_csv("schools/survey_all.txt",encoding = "windows-1252", delimiter="\t")
d75_survey = pd.read_csv("schools/survey_d75.txt",encoding = "windows-1252", delimiter="\t")
survey = pd.concat([all_survey,d75_survey],axis=0)
print(survey.head(5))

## 8. Cleaning up the surveys ##

relevant_columns = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11",]
survey["DBN"] = survey["dbn"]
survey = survey[relevant_columns]
data['survey']=survey
print(data['survey'].shape)


## 9. Inserting DBN fields ##

def customePad(number):
    strnumber = str(number)
    numlen =  len(strnumber)
    if numlen==1:
        return strnumber.zfill(2)
    return strnumber
        
hs_directory =  data['hs_directory']
hs_directory['DBN']=hs_directory['dbn']
data['class_size']['padded_csd']=data['class_size']['CSD'].apply(customePad)
data['class_size']['DBN']=data['class_size']['padded_csd']+data['class_size']['SCHOOL CODE']
print(data['class_size']['DBN'].head())

## 10. Combining the SAT scores ##

sat_results = data['sat_results']
sat_results['SAT Math Avg. Score']=pd.to_numeric(sat_results['SAT Math Avg. Score'],errors="coerce")
sat_results['SAT Critical Reading Avg. Score']=pd.to_numeric(sat_results['SAT Critical Reading Avg. Score'],errors="coerce")
sat_results['SAT Writing Avg. Score']=pd.to_numeric(sat_results['SAT Writing Avg. Score'],errors="coerce")
sat_results['sat_score']=sat_results['SAT Critical Reading Avg. Score'] + sat_results['SAT Math Avg. Score'] + sat_results['SAT Writing Avg. Score']
print(sat_results['sat_score'].head())

## 11. Parsing coordinates for each school ##

import re
def latlong(location1):
    latlongc= re.findall("\(.+, .+\)", location1)
    #print(type(latlongc))
    latlongstr = latlongc[0].replace('(','').replace(')','')
    lat = latlongstr.split(',')[0]
    return lat
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(latlong)
print(data['hs_directory'].head())
                                     
    

## 12. Extracting the longitude ##

import re
def latlong(location1):
    latlongc= re.findall("\(.+, .+\)", location1)
    #print(type(latlongc))
    latlongstr = latlongc[0].replace('(','').replace(')','')
    lat = latlongstr.split(',')[1]
    return lat
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(latlong)

data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'],errors="coerce")
data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'],errors="coerce")
print(data['hs_directory'].head())
    