# Data Collection, Understanding, and Cleaning

## Introduction

In the initial phase of our project, we focus on collecting, understanding, and cleaning the dataset. This is a crucial step in building a reliable predictive model for suburban house pricing in King County, Washington.

## Challenges

The challenges in the real estate market are multifaceted. Real estate agencies often grapple with two primary issues: overpricing and the lack of a robust decision framework. Overpricing can lead to properties remaining unsold for prolonged periods, incurring additional costs, and diminishing potential profits. On the other hand, prospective buyers face difficulties in determining which properties align with their budgets and desired features.

## Objectives

The core problem that our project addresses is to provide a suburban house pricing model that considers the features of a house to determine its value. Overpricing can be detrimental to both sellers and buyers. The absence of a reliable decision framework means that clients with varying budgets and preferences lack guidance in their property search. Therefore, our objectives are as follows:

a) Build a regression model that can predict suburban house prices with an accuracy of at least 75%, ensuring that the predictions are within a range of $75,000 from the actual prices.

b) Identify Key Factors Influencing House Prices in King County, California, to provide valuable insights for precise pricing strategies.

c) Analyze Model Performance using metrics such as mean squared error, R-squared values, and residual analysis to gauge the model's effectiveness.

d) Provide Actionable Recommendations to the Real Estate Agency for improving profitability and market presence, leveraging insights from the model.

## 1. Imported Libraries

The relevant libraries were imported to assist with data manipulation, visualization, and modeling.

## 2. Imported Dataset

We loaded the dataset into a Pandas dataframe. This dataset is crucial for building our predictive model.

## 3. Data Understanding

### 3.1 Key Data Columns

We explored the characteristics of the dataset, understanding the key columns that will play a vital role in our analysis. These include the following columns:

- Date – Date the house was sold
- Price – Sale price (prediction target)
- Bedrooms – Number of bedrooms
- Bathrooms – Number of bathrooms
- Sqft_living – Square footage of living space in the house
- Sqft_lot – Square footage of the lot
- Floors – Number of floors (levels) in the house
- Sqft_above – Square footage of the house apart from the basement
- Sqft_basement – Square footage of the basement
- Yr_built – Year when the house was built
- Yr_renovated – Year when the house was renovated
- Lat – Latitude coordinate
- Long – Longitude coordinate
- Sqft_living15 – The square footage of interior housing living space for the nearest 15 neighbors
- Sqft_lot15 – The square footage of the land lots of the nearest 15 neighbors

## 4. Data Cleaning

### 4.1 Handling Missing Values

We addressed missing values in the dataset and ensured data cleanliness:

- Waterfront missing values were replaced with the mode of the houses grouped by zipcode.
- View missing values were replaced with the mode of the houses grouped by zipcode.
- Yr_renovated column missing values were replaced with 0. It is assumed that if this metric is not there, then the house has never been renovated.

### 4.2 Detecting Duplicates

We checked for duplicate entries in the dataset. Fortunately, there were no duplicates found.

### 4.3 Fixing Data Types

We corrected the data types in the dataset, particularly changing the 'sqft_basement' column from an object to a numeric value (float).

### 4.4 Outlier Detection

We also examined the dataset for outliers in all columns.

This section lays the foundation for our data analysis and modeling efforts. With a clean and well-understood dataset, we are ready to proceed to the next stages of our project.

# Data Preparation and Feature Engineering

## 5.0 Introduction

In this section, we dive into data preparation and feature engineering, a crucial part of the data science workflow. Here, we shape and enhance the dataset, making it more suitable for modeling and analysis.

## 5.1 Adding New Columns

In this sub-section, we introduce new columns to enrich our dataset:

### 5.1.1 Adding an Age Column

We've calculated the age of each house by subtracting the sale date from either the year built or year renovated. Some houses might have negative ages, and these were subsequently dropped from the dataset.

### 5.1.2 Adding a Renovated Column

A new column is added to indicate whether a house has been renovated or not.

### 5.1.3 Adding a Total Square Footage Column

We've created a new column, 'total_square_footage,' by summing the square footage of living space ('sqft_living') and the square footage of the basement ('sqft_basement').

### 5.1.4 Adding a Price per Square Foot Column

We've added a 'price_per_square_feet' column by dividing the house's price by its total square footage.

### 5.1.5 Adding an Average Price per Zipcode Column

By grouping houses by their zipcodes, we calculated the average price for each zipcode, providing valuable insights.

### 5.1.6 Adding a Has Basement Column

A new column, 'has_basement,' is created using a lambda function that checks if the basement column has any value other than zero. Houses with basements were assigned a value of 1, and those without received a value of 0.

## 5.2.1 Dropping Columns

We've sorted all numeric columns based on their correlation with the price. Columns with a correlation less than 0.3 and not deemed essential for modeling were dropped. These columns include 'has_basement,' 'yr_renovated,' 'renovated,' 'sqft_lot,' 'sqft_lot15,' 'yr_built,' 'long,' 'lat,' 'is,' 'zipcode,' and 'age.'

## 5.3 Ordinal Encoding

We've performed ordinal encoding on specific columns, such as 'grade,' 'condition,' and 'view.' Dictionaries were created based on the unique values in each column to facilitate encoding.

## 5.4 One-Hot Encoding

The 'waterfront' column underwent one-hot encoding, ensuring it didn't suffer from the dummy variable trap.

These data preparation and feature engineering steps aim to make the dataset more suitable for modeling and analysis. The dataset is now ready for further stages of our project.

# Data Cleaning, Outlier Removal, and Bivariate Analysis

## 5.5 Removing Outliers

In this section, we focused on identifying and handling outliers within the dataset. We've developed a function that takes the dataset and a dictionary of columns along with the quantile to create a mask for filtering the dataset, resulting in a new dataset with outliers removed. Key columns that underwent outlier removal include 'price,' 'sqft_living,' 'bedrooms,' and 'sqft_above.'

## 5.6 Bivariate Analysis

In this sub-section, we performed bivariate analysis, which explores the relationships between two variables. We created a versatile function that generates various types of plots for each column and its relationship with the 'price' column. This analysis provides valuable insights into how features relate to the target variable.

### 5.6.1 Heatmaps

Two types of heatmaps were added: a triangular heatmap and a rectangular heatmap. These heatmaps visualize the correlations between different features and the 'price.' They help us identify strong and weak relationships.

### 5.6.2 Top Features in Relation to Price

A barplot was created to showcase the top features in terms of their relationship to the 'price.' These features are arranged in descending order, providing a clear understanding of their impact on house prices.

These data cleaning and bivariate analysis steps are essential in preparing the dataset for modeling and gaining insights into feature importance. The dataset is now more refined and ready for further analysis.

# Regression Modeling

## 6.0 Introduction

In this section, we dive into the heart of our project - regression modeling. Our goal is to build predictive models to estimate suburban house prices in King County, Washington accurately. This phase is crucial for achieving our project objectives.

## 6.1 Creating Base Models

In this sub-section, we started by creating a base model. We used the Ordinary Least Squares (OLS) method in statsmodels and included the 'average_price_per_zipcode' feature. The model achieved an R-squared value of 46.8 and was statistically significant. Additionally, we created a similar model using Scikit-Learn, with a Mean Absolute Error (MAE) of 124,066 and a Root Mean Squared Error (RMSE) of 169,337.

## 6.2 SKLEARN with Data Transformation

In this part, we introduced a pipeline and a param_grid for hyperparameter tuning using GridSearchCV in Scikit-Learn. The results were comparable to the base models.

## 6.3 Multiple Linear Regression

We expanded our model by including other features that demonstrated significant relationships with the 'price' column. This new model produced impressive results with an MAE of 49,852 and an R-squared value of 90.4. To mitigate collinearity, we dropped some columns, resulting in a final model with an R-squared score of 83.1.

## 6.4 Regression Line

In this section, we created a regression line to visualize the relationships between features and the 'price.'

## 6.5 Residual Plot

We plotted a residual plot to assess the performance of our models.

## What You Should Know

When using this repository on GitHub, here's what you need to know:

### Running the Code

To run the code and replicate the analysis, you'll need Python installed along with the necessary libraries. You can follow these steps:

1. Clone this repository to your local machine.

2. Ensure you have Python installed, along with libraries like Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, and Scikit-Learn.

3. Follow the Jupyter Notebook files in the repository to walk through the project step by step. 

4. To run specific sections of the code, follow the instructions provided within the notebooks.

### Data and Models

The project contains data files and Jupyter notebooks that walk you through the entire analysis process. You can access and explore the data used for modeling as well as the trained models. You can also create and evaluate your own models based on the provided code.

### Hyperparameter Tuning

If you want to fine-tune model hyperparameters, refer to the code in the GridSearchCV section. You can modify the parameters and grid values as needed.

### Customization

Feel free to customize and adapt the code to your specific project needs. We've provided a foundation for regression modeling, and you can build upon it based on your own dataset and objectives.


