Chapter 1: Business Overview


1.1   Introduction

The real estate market is a complex and dynamic environment where accurately pricing houses is of paramount importance. In this ever-changing landscape, homeowners, buyers, and real estate agencies are often faced with the challenge of determining the fair market value of a property. The consequences of inaccurate pricing can be significant, ranging from houses languishing on the market for extended periods to missed opportunities for maximizing profit.

The quest for a precise and data-driven solution to this challenge has led us to explore the application of a multilinear regression model. By leveraging the power of data analysis and predictive modeling, we aim to provide a practical tool that can revolutionize the way houses are priced, making the process more transparent, efficient, and informed.


1.2   Challenges

The challenges in the real estate market are multifaceted. Real estate agencies often grapple with two primary issues: overpricing and the lack of a robust decision framework. Overpricing can lead to properties remaining unsold for prolonged periods, incurring additional costs, and diminishing potential profits. On the other hand, prospective buyers face difficulties in determining which properties align with their budgets and desired features.


1.3    Problem Statement

The core problem that our project addresses is the accurate pricing of houses listed in the market. Overpricing can be detrimental to both sellers and buyers. The absence of a reliable decision framework means that clients with varying budgets and preferences lack guidance in their property search. As such, there is a clear need for a data-driven solution that can provide precise house price predictions and, in doing so, mitigate the challenges faced by stakeholders in the real estate market.

1.3.1        Objectives

a). Develop a multilinear regression model with the highest possible accuracy to predict and determine house prices based on their features.

b). Identify Key Factors Influencing House Prices in King County, California, to provide valuable insights for precise pricing strategies.

c). Analyze Model Performance using metrics such as mean squared error, R-squared values, and residual analysis to gauge the model's effectiveness.


d). Provide Actionable Recommendations to the Real Estate Agency for improving profitability and market presence, leveraging insights from the model.



Chapter 2: Data Understanding

2.1 Numerical Variables

To better understand the dataset we identified the numeric variables .We intend to drop columns that have low correlation with the dependent variable .They include latitude and longitude.

Date – Date house was sold

Price – Sale price(prediction target)

Bedrooms – Number of bedrooms

Bathrooms – Number of bathrooms

Sqft_living – Square footage of living space in the house

Sqft_lot – Square footage of the lot

Floors – Number of floors(levels) in the house

Sqft_above – Square footage of the house apart from the basement.

Sqft_basement – Square footage of the basement.

Yr_built – Year when house was built.

Yr_renovated – Year when house was renovated.

Lat – Latitude coordinate.

Long – Longitude coordinate.

Sqft_living15 – The square footage of interior housing living space for the nearest 15 neighbors.

Sqft_lot15 – The square footage of the land lots of the nearest 15 neighbors.

2.1 Numerical columns 


2.2 Categorical Variables

We also identified the categorical variables and described them to better understand the dataset.

Waterfront – Whether the house is on a waterfront
View –Quality of view from house
Condition –How good the overall condition of the house is. Related to maintenance of house.
Grade – Overall grade of the house. Related to the construction and design of the house.
Zipcode – ZIP Code used by the United States Postal Service.


Chapter 3: Data Cleaning

In this chapter, we will focus on preparing the dataset for analysis and modeling by performing the following key steps:

3.1 Identifying and Handling Duplicates

In this initial step, we will identify and remove any duplicate entries in the dataset. Duplicates can skew our analysis and modeling results, so it's essential to ensure data integrity.

3.2 Handling Missing Values

After exploring the dataset, we have discovered missing values in several columns, including 'Waterfront,' 'yr_renovated,' and 'views.' These missing values need to be addressed to maintain the dataset's integrity. Our approach will include:

3.2.1 Waterfront Column

For the 'Waterfront' column, we will handle missing values by replacing them with the mode (the most frequent value). This is a common approach for categorical data where the majority class provides the best approximation for the missing data.

3.2.2 Year Renovated Column

In the 'yr_renovated' column, we will perform feature engineering to classify houses as either renovated or not renovated. This transformation will help us retain the valuable information about renovations without relying on incomplete data.

3.2.3 Views Column

For the 'views' column, we will determine the best approach to handle the missing values, considering the nature of the data and its impact on our model.

These feature engineering and selection steps are essential to ensure that our model is built on the most relevant and informative data, allowing it to make accurate predictions. By systematically addressing duplicates, missing values, and selecting the most relevant features,, our dataset will be primed for effective exploratory data analysis (EDA) and modeling in the subsequent chapters.


Chapter 4: EDA & Feature Engineering 

4.1 EDA

4.1.1 Univariate

4.1.2 Bivariate

4.1.3 Multivariate


4.2 Feature Engineering

In this step, we will not only identify and remove irrelevant columns but also create new features that enhance the predictive power of our model. Our approach will include:

3.3.1 Handling 'yr_renovated' and Creating a ‘renovated’ column

For the 'yr_renovated' column, we will engineer a new feature (renovated) that classifies houses as either "renovated" or "not renovated." This transformation will allow us to capture the impact of renovations on house prices, even when the exact renovation year is missing.

3.3.2 Calculating House Age and Dropping the 'date' Column

To gain insights into the age of the houses, we will utilize the 'date' column, which contains information about when the house was built. We will calculate the age of each house by subtracting the construction year from the current date. After calculating the age, we will drop the 'date' column from the dataset to streamline it and remove redundant information.

Chapter 4: Data Analysis and Modelling

Chapter 5: Conclusion

Chapter 6: Limitation Next Steps

Appendix

