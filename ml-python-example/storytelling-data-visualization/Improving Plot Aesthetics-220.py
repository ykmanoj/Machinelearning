## 2. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#women_degrees.plot(x='Year',y='Biology',kind='line')
plt.plot(women_degrees['Year'],women_degrees['Biology'])

## 3. Visualizing The Gender Gap ##

import pandas as pd
import matplotlib.pyplot as plt

#women_degrees.plot(x='Year',y='Biology',kind='line')
plt.plot(women_degrees['Year'],women_degrees['Biology'], label= "Women", color="blue")
plt.plot(women_degrees['Year'],100-women_degrees['Biology'], label= "Men", color="green")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc= "upper right")
plt.show()

## 5. Hiding Tick Marks ##

import pandas as pd
import matplotlib.pyplot as plt

#women_degrees.plot(x='Year',y='Biology',kind='line')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(women_degrees['Year'],women_degrees['Biology'], label= "Women", color="blue")
ax.plot(women_degrees['Year'],100-women_degrees['Biology'], label= "Men", color="green")
ax.tick_params(bottom="off",top="off",left="off",right="off")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc= "upper right")
plt.show()

## 6. Hiding Spines ##

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Add your code here
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)

ax.spines["bottom"].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

## 7. Comparing Gender Gap Across Degree Categories ##

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.
    plt.xlim(1968,2011)
    plt.ylim(0,100)
    plt.title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    for key,spine in ax.spines.items():
        spine.set_visible(False)

# Start solution code.

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()