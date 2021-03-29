import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df["weight"]/((df["height"]/100)**2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"]= df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df.loc[df["gluc"]==1, "gluc"] = 0
df.loc[df["gluc"]>1, "gluc"] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars="cardio")




    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x = "variable", hue = "value", col = "cardio", data = df_cat, kind = "count").set_axis_labels("variable", "total")
    fig = g.fig
    
  


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= (df['height'].quantile(0.025))) &
    (df['height'] <= (df['height'].quantile(0.975))) &
    (df['weight'] >= (df['weight'].quantile(0.025))) &
    (df['weight'] <= (df['weight'].quantile(0.975)))
    ]

    # Calculate the correlation matrix
    # https://heartbeat.fritz.ai/seaborn-heatmaps-13-ways-to-customize-correlation-matrix-visualizations-f1c49c816f07
    
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    # NumPy array creation: triu() function
    # Upper triangle of an array. The triu() function is used to get a copy of a matrix with the elements below the k-th diagonal zeroed.March 28, 2021
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,annot=True, fmt='.1f', linewidths=1, mask=mask, vmax=.3, center=0,square=True, cbar_kws = {'shrink':0.5})



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
