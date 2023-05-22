# Data-Visualization

## What were the objectives? 

1. improve work with data visualisation libraries 
    
2. improve work with tables and their grouping
    
3. touch a bit of machine learning ( linear regression ) in the visualisation of finding a linear relationship
    
## Data Research

At first there were 6 countries in my data table: USA, China, Germany, Mexico, Zimbabwe and Chile. 
Each country had 15 years of GDP and life expectancy data. 

But first, what is *_GDP_*?
GDP measures the monetary value of final goods and services. 
In simple terms, the higher the GDP, the better life in the country.
If you have more questions about GDP, you can read [this article](https://www.imf.org/en/Publications/fandd/issues/Series/Back-to-Basics/gross-domestic-product-GDP#:~:text=GDP%20measures%20the%20monetary%20value,the%20borders%20of%20a%20country.).

### 1. GDP Development

The **first** thing I found was that only three countries had positive GDP growth from 2000 to 2015: the United States, China and Germany. 
But the latter was barely noticeable. 

![image](https://github.com/DmiPy/Data-Visualization/assets/128055633/d5cfaa75-c80c-4e8c-ad0b-1fcb5383c84f)


### 2. Correlation between life expectancy and GDP

**Next we look at the correlation between life expectancy and GDP. Here we see a linear relationship in all countries. 
Every year in all countries, GDP increased slightly with life expectancy.** 

The only difference is that some countries (e.g. Germany) had a life expectancy of 78 years in 2000, while Zimbabwe started at 44 years at the same time.

![corr_lifeexp_gdp](https://github.com/DmiPy/Data-Visualization/assets/128055633/757ae337-5789-4785-9f16-0225b52320bf)

### 3. Top countries by GDP and life expectancy

The **third** visualisation shows the _top countries by GDP and life expectancy_. It is obvious that eight years ago the **_USA dominated GDP_**. 
Even China could not compete with the United States at that time. Of course, we know that the situation has changed dramatically since then, 
but the information we have is up to 2015.

What about **life expectancy**? Here we can see that although the US has the highest GDP, it does not look like it is going to break away. Germany is by far the leader here, with a GDP lower than China's. 
**The conclusion is that GDP has no direct effect on life expectancy._**

![top_life_expectancy_gdp](https://github.com/DmiPy/Data-Visualization/assets/128055633/3a00c165-5a01-44e6-925b-1e31f5847aef)


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

It was difficult because it required knowledge of linear regression. It also did not meet my expectations because 
as I found out in [point 3](https://github.com/DmiPy/Data-Visualization/edit/main/README.md#3-top-countries-by-gdp-and-life-expectancy), there is no correlation or relationship between life expectancy and GDP. 
You could say that a linear relationship also requires a lot more data than about 100 lines. 

So here we can clearly see that a ***_linear regression is not suitable or simple to determine or predict the relationship between GDP and life expectancy._***. 
![linmodel](https://github.com/DmiPy/Data-Visualization/assets/128055633/48306539-f621-4685-812e-101144331ac3)


## Conclusion. 

Although certain conclusions have been made about the fact that **_there is no correlation between life expectancy and GDP_**, _we *cannot* say that this is *100%* true_. 
After all, the information in my table is rather limited, because it contains only 6 countries from different continents with a time period of 15 years. That's not enough to draw confident conclusions. 
Moreover, linear regression is not appropriate for this case. A more sophisticated machine learning method is needed here, which I do not yet possess. 


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



    
    
    
