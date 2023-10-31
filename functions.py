# This is a functions files

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno



def handling_missing_values(df, column_name):
    # Group the DataFrame by 'zipcode' and calculate the mode for the specified column

    mode_by_zipcode = df.groupby('zipcode')[column_name].apply(lambda x: x.mode().iloc[0])
    
    # Fill missing values in the specified column based on the 'zipcode' mode
    df[column_name] = df.apply(lambda row: mode_by_zipcode[row['zipcode']] if pd.isna(row[column_name]) else row[column_name], axis=1)

# handling_missing_values()

def fill_missing_with_mode(df, group_by_column, target_column):
    # Group the DataFrame by the specified column and calculate the mode for the target column within each group
    mode_by_group = df.groupby(group_by_column)[target_column].agg(lambda x: x.mode().iloc[0])

    # Fill missing values in the target column based on the mode within each group
    for index, row in df.iterrows():
        if pd.isna(row[target_column]):
            df.at[index, target_column] = mode_by_group[row[group_by_column]]



def create_box_plot(data, column):
 
    # Create a single subplot
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot the box plot
    sns.boxplot(x=data[column], ax=ax, orient='h')
    
    # Set the title and x-label based on the column name
    ax.set_title(f'Box Plot of {column}')
    ax.set_xlabel(column)
    
    return ax