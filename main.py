import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm 
from sklearn.model_selection import train_test_split

df = pd.read_csv("all_data.csv")    # df is a dataframe containing the data of each country's GDP and Live Expectancy
df["Country"] = df["Country"].replace("United States of America", "USA")

chile = df[df.Country == "Chile"]                   # dividing the dataframe into individual countries
germany = df[df.Country == "Germany"]
mexico = df[df.Country == "Mexico"]
us = df[df.Country == "United States of America"]
zimbabwe = df[df.Country == "Zimbabwe"]
china = df[df.Country == "China"]

# task 1:
# Comparison of life expectancy and GDP:
# Construct a graph showing life expectancy and GDP for each country over a period of time.
# Such a graph will allow us to compare trends and possible correlations between the two indicators.

sns.lmplot(data=df, x="Year", y="GDP", lowess=True,               # using linear model plot to show the correlation between
           hue="Country", palette="colorblind")                   # countries' GDP
plt.show()
plt.close()

# task 2:
# Correlation between life expectancy and GDP:
# Investigate the correlation between life expectancy and GDP for each country.
# Construct a scatter plot to see if there is a relationship between the two indicators.
# A correlation coefficient can also be calculated to quantify the relationship between the two.

countries = df['Country'].unique()                                  # creating labels for each country
colors = ["orange", "red", "black", "green", "blue", "#f5d442"]     # creating color for each country

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))         # creating a figure with 2 rows and 3 columns
fig.suptitle("Correlation between Life Expectancy and GDP")         # with figure size 12x8

for i, country in enumerate(countries):                             # using a loop 6 scatterplots for each country will be created
    cols = i % 3                                                    # remainder of division: column position
    rows = i // 3                                                   # integer division: row position                                        
    ax = axes[rows, cols]                                           # position in figure
    country_data = df[df.Country == country]    
    x_values = [x for x in range(                                   # creating start x labels
        len(country_data["Life expectancy at birth (years)"]))]
    rounded_values = [                                              # round the values on the x-axis because they are float
        round(value) for value in country_data["Life expectancy at birth (years)"]]
    sns.regplot(country_data, ax=ax,                                # regplot shows the correlation between Life Expectancy
                    x="Life expectancy at birth (years)", y="GDP", color=colors[i]) # and GDP. Each Country has its own color
    ax.set_xticks(rounded_values)                                   # replacing the start x labels with rounded values
    if len(set(rounded_values)) > 8:                                # if there are too many labels on x axis, they will be rotated
        ax.set_xticklabels(ax.get_xticklabels(), rotation=35)

    ax.set_title(f"{country}")                                      # title and labels
    ax.set_xlabel("Life expectancy at birth (years)")
    ax.set_ylabel("GDP")

plt.tight_layout()                                                  # adjusts the position and size of the charts on the figure
plt.show()
plt.close()

# task 3:
# Top countries by life expectancy and GDP:
# Identify the top country with the longest life expectancy and highest GDP.
# Construct a bar chart or pie chart to visualise this comparison.

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))  # creating a figure with 2 rows and 2 columns with
plt.suptitle("Top countries by Life Expectancy and GDP")      # figure size 10x10

ax = axes[0, 0] # position in the figure is 0,0 
sns.barplot(data=df, x="Country", y="GDP", errorbar=("pi", 50), capsize=.4, errcolor=".5",
            linewidth=3, edgecolor=".5", ax=ax) # connecting the barplot and the position in figure
ax = axes[0, 1]
sns.barplot(data=df, x="Country", y="Life expectancy at birth (years)",
            linewidth=3, ax=ax)

grouped_GDP = df.groupby('Country')["GDP"].median()         # group by country and GDP values
labels = grouped_GDP.index                                  # labels for each country
axes[1, 0].pie(grouped_GDP, labels=None, autopct="")        # no labels because they overlap each other
axes[1, 0].axis("equal")                                    # make pie to be a circle                
axes[1, 0].legend(labels, title="Countries", loc="best")    # instead of labels there is a legend

grouped_Life_Expectancy = df.groupby(                       # group by country and Live Expectancy values
    'Country')["Life expectancy at birth (years)"].median()
labels = grouped_Life_Expectancy.index
axes[1, 1].pie(grouped_Life_Expectancy, labels=labels, autopct="%.1f%%")
axes[1, 1].axis("equal")
axes[1, 1].legend(title="Countries", loc="center left")

plt.tight_layout()      # adjusts the position and size of the charts on the figure
plt.show()
plt.close()

# task 4:
# Grouping and Comparison:
# Group countries into continents or other categories and compare life expectancy and GDP between groups.
# Construct bar plots or box plots for visual comparison.

# dividing countries into continents and adding a new column: Continent
eurasia = [germany, china]
eurasia = pd.concat(eurasia)
eurasia["Continent"] = "Eurasia"

america = [chile, us, mexico]
america = pd.concat(america)
america["Continent"] = "America"

africa = zimbabwe
africa["Continent"] = "Africa"

# combine all the divided tables to create one barplot
combined_table = pd.concat([eurasia, america, africa])

fig, axes = plt.subplots(nrows=2, ncols=2) # creating figure with 2 rows and 2 columns
sns.set_palette("colorblind")
ax = axes[0, 0]
sns.barplot(data=combined_table, x="Continent", y="GDP", errorbar="sd", ax=ax)

ax = axes[0, 1]
sns.barplot(data=combined_table, x="Continent",
            y="Life expectancy at birth (years)", errorbar="sd", ax=ax)

ax = axes[1, 0]
sns.boxplot(data=combined_table, x="Continent", y="GDP", ax=ax)

ax = axes[1, 1]
sns.boxplot(data=combined_table, x="Continent",
            y="Life expectancy at birth (years)", ax=ax)

plt.tight_layout()  # adjusts the position and size of the charts on the figure
plt.show()
plt.close()

# task 5:
# Regression analysis:
# Use linear regression or other machine learning models to predict life expectancy based on GDP.
# Plot the regression line and evaluate the quality of the model.

# the column name is too long
df.rename(columns={"Life expectancy at birth (years)": "Life_Expectancy"},
          inplace=True, errors='raise')

# dividing data into GDP and life expectancy
x = df[['GDP']]
y = df['Life_Expectancy']

# dividing the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# linear regression model
model = sm.OLS(y_train, x_train).fit()

y_pred = model.predict(x_test)

# how good the model is
r_squared = model.rsquared
# mean square error
mse = model.mse_resid

# drawing a graph with raw data
plt.scatter(x_test, y_test, color='blue', label='Actual')

# building the regression line
plt.plot(x_test, y_pred, color='red', linewidth=2, label='Predicted')

# adding labels and legend
plt.title(
    f"""
    R-squared: {r_squared}
    mean square error: {mse}
"""
)
plt.xlabel('GDP')
plt.ylabel('Life Expectancy')
plt.legend()

# displaying graph
plt.show()
plt.close()

# calculating residuals 
residuals = y_test - y_pred

# displaying graph of residuals
plt.scatter(y_pred, residuals, color='green')

# adding horizontal line on level 0
plt.axhline(y=0, color='red', linestyle='--')

# adding labels
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')


# graph display
plt.show()
plt.close()

# there is no linear relationship between GDP and Live Expectancy values
