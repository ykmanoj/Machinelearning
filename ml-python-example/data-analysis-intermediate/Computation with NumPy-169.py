## 2. Array Comparisons ##

years_1984 = (world_alcohol[:,0] == "1984")
countries_canada = (world_alcohol[:,2] == "Canada")

## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2]=='Algeria'
country_algeria = world_alcohol[country_is_algeria] 

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0]=='1986') & (world_alcohol[:,2]=='Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986]

## 5. Replacing Values ##

row_1986 = world_alcohol[:,0]=='1986'
world_alcohol[row_1986,0] = '2014'

wine_grog= world_alcohol[:,3]=='Wine'
world_alcohol[wine_grog,3]='Grog'

## 6. Replacing Empty Strings ##

is_value_empty=world_alcohol[:,4]==''
world_alcohol[is_value_empty,4]='0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986 =world_alcohol[(world_alcohol[:,0]=='1986') & (world_alcohol[:,2]=='Canada')]
canada_1986[canada_1986[:,4]==''] = '0'
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()


## 10. Calculating Consumption for Each Country ##

totals = {}
for country in countries:
    world_alcohol_country = world_alcohol[(world_alcohol[:,2]==country) &   (world_alcohol[:,0]=='1989')]
    print(world_alcohol_country)
    alochol_cunsumption = world_alcohol_country[:,4].astype(float)
    print(alochol_cunsumption)
    total_country_alcohol = alochol_cunsumption.sum()
    totals[country]=total_country_alcohol

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
totals = {}
for country in countries:
    world_alcohol_country = world_alcohol[(world_alcohol[:,2]==country) &   (world_alcohol[:,0]=='1989')]
    print(world_alcohol_country)
    alochol_cunsumption = world_alcohol_country[:,4].astype(float)
    print(alochol_cunsumption)
    total_country_alcohol = alochol_cunsumption.sum()
    if highest_value < total_country_alcohol:
        highest_value = total_country_alcohol
        highest_key = country
    totals[country]=total_country_alcohol
