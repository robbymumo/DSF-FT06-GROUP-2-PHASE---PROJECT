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

