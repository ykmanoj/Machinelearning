## 2. Introduction to the data ##

cars_name=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name']
cars=pd.read_table("auto-mpg.data",delim_whitespace=True,names=cars_name,header=None)

print(cars)

## 3. Exploratory data analysis ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
cars.plot("weight", "mpg", kind='scatter', ax=ax1)
cars.plot("acceleration", "mpg", kind='scatter', ax=ax2)
plt.show()

## 5. Scikit-learn ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars["mpg"])
predictions=lr.predict(cars[['weight']].values)
print(predictions[0:5])
print(cars["mpg"][0:5])

## 6. Making predictions ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars["mpg"])
predictions=lr.predict(cars[['weight']].values)
print(predictions[0:5])
print(cars["mpg"][0:5])

## 7. Plotting the model ##

plt.scatter(cars["weight"], cars["mpg"], c='red')
plt.scatter(cars["weight"], predictions, c='blue')

## 8. Error metrics ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars["mpg"])
predictions=lr.predict(cars[['weight']].values)
print(predictions[0:5])
print(cars["mpg"][0:5])

## 9. Root mean squared error ##

mse = mean_squared_error(cars["mpg"], predictions)
rmse=numpy.sqrt(mse)
print(rmse)