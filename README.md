# Data-Visualization

## What were the goals? 

1. to hone work with libraries for data visualization 
    
2. to improve work with tables and their grouping
    
3. to touch a little bit of machine learning ( linear regression ) in the visualization of finding a linear relationship
    
## Data Research

First, there were 6 countries in my data table: USA, China, Germany, Mexico, Zimbabwe, Chile. 
Each country had 15 years of GDP and Life Expectancy data. 

But first, what is *_GDP_*?
GDP measures the monetary value of final goods and services. 
Simply speaking, the higher the GDP, the better the life in the country.

### 1. GDP Development

The **first** thing I found was that from 2000 to 2015, only three countries had positive GDP development: the United States, China, and Germany. 
But the last one was hardly noticeable. 

![image](https://github.com/DmiPy/Data-Visualization/assets/128055633/d5cfaa75-c80c-4e8c-ad0b-1fcb5383c84f)


### 2. Correlation between life expectancy and GDP

**Next** is the correlation between life expectancy and GDP. Here we observe a linear relationship in all countries. 
Every year in all countries the GDP with life expectancy increased slightly. 

The only difference is that some country (say Germany) had a life expectancy of 78 years in the year 2000, while Zimbabwe started at 44 years at the same time.

![corr_lifeexp_gdp](https://github.com/DmiPy/Data-Visualization/assets/128055633/757ae337-5789-4785-9f16-0225b52320bf)

### 3. Top countries by GDP and life expectancy

The **third** visualization shows the _top countries by GDP and life expectancy_. Obviously, eight years ago, the **_U.S. dominated GDP_**. 
Even China at that time could not be competitive with the United States. Of course we know that the situation has changed dramatically now, 
but the information we have is up to 2015.

What about **life expectancy**? Here we can see that even though the U.S. has the highest GDP, it does not look like it is breaking away. Germany is by far the leader here, with a GDP lower than that of China. 
**_The conclusion is that GDP has no direct effect on life expectancy._** 

![image](https://github.com/DmiPy/Data-Visualization/assets/128055633/6d69d5c3-579b-4916-9e5f-0deec5fab404)


### 4. Grouping and Comparison

In the 4 visualization I divided all 6 countries into continents: 

* America 
    + USA 
    + Mexico  
    + Chile
* Eurasia 
    + Germany 
    + China 
* Africa 
    + Zimbabwe

Since Mexico and Chile do not have much GDP, this leaves America with about as much GDP as it originally had. But in Eurasia the situation is more interesting, because the two countries together (Germany and China) exceed America's GDP. As for Zimbabwe, there is no chance.

![over_countintents](https://github.com/DmiPy/Data-Visualization/assets/128055633/4d4bdc62-d20f-4903-9c84-5952f5ce571c)


### 5. Regression analysis

The last and most difficult part for me: Regression analysis

It was difficult because it required knowledge of linear regression. Moreover, it did not meet my expectations, because, 
as I found out in [point 3](https://github.com/DmiPy/Data-Visualization/edit/main/README.md#3-top-countries-by-gdp-and-life-expectancy), there is no correlation or relationship between life expectancy and GDP. 
You could say that a linear relationship also requires a lot more data than about 100 lines. 

So here we can clearly see that a ***_linear regression is not suitable or cannot simply determine or predict the relationship between GDP and life expectancy._*** 

![linmodel](https://github.com/DmiPy/Data-Visualization/assets/128055633/48306539-f621-4685-812e-101144331ac3)


## How to install the project ?
1. Create a github.com account if you don't have one

2. Clone the [origin](https://github.com/DmiPy/Data-Visualization) repository to your local computer using the following command:

    ```$ git clone https://github.com/DmiPy/Data-Visualization.git```

3. Install all the neccessary libraries with `pip` or `anaconda`

    * ```pip install pandas```

    * ```pip install matplotlib```

    * ```pip install statsmodels```

    * ```pip install scikit-learn```

    * ```pip install seaborn```


4. Open the project and that's it!



    
    
    
