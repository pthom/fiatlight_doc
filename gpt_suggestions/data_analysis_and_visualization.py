"""
Data Analysis and Visualization

Scenario: A data scientist wants to quickly analyze and visualize a dataset.
Use Case: Using Fiatlight, they can create an interactive application that allows users to load datasets, perform exploratory data analysis (EDA), and visualize results with custom plots.
Example Code:
"""

import fiatlight as fl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Define a function to load and display a dataset
def load_dataset(file_path: fl.fiat_types.TextPath) -> pd.DataFrame:
    return pd.read_csv(file_path)

# Define a function to plot data
def plot_data(data: pd.DataFrame, column: str) -> Figure:
    fig, ax = plt.subplots()
    data[column].hist(ax=ax)
    ax.set_title(f'Distribution of {column}')
    return fig

# Run the application
fl.run([load_dataset, plot_data], app_name="Data Analysis")