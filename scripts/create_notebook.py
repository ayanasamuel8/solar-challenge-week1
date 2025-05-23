import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

# Add markdown cell with title
nb['cells'] = [nbf.v4.new_markdown_cell('''# Solar Radiation Data Analysis: Benin, Sierra Leone, and Togo

This notebook compares solar radiation metrics (GHI, DNI, DHI) across three countries:
- Benin
- Sierra Leone
- Togo''')]

# Add imports cell
imports = '''# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set style for better visualizations
plt.style.use('default')
sns.set_palette('husl')
plt.rcParams['figure.figsize'] = [12, 8]

# Display all columns
pd.set_option('display.max_columns', None)'''

nb['cells'].append(nbf.v4.new_code_cell(imports))

# Add data loading cell
data_loading = '''def load_country_data(country_name):
    """Load data for a specific country."""
    filename = f'../../data/{country_name.lower().replace(" ", "_")}_clean.csv'
    df = pd.read_csv(filename)
    df['Country'] = country_name
    print(f"Successfully loaded data for {country_name}")
    return df

# Load data for all countries
countries = ['Benin', 'Sierra Leone', 'Togo']
dfs = []

for country in countries:
    try:
        df = load_country_data(country)
        dfs.append(df)
    except Exception as e:
        print(f"Error loading data for {country}: {str(e)}")

# Combine all dataframes
combined_df = pd.concat(dfs, ignore_index=True)
combined_df.head()'''

nb['cells'].append(nbf.v4.new_code_cell(data_loading))

# Add distribution analysis section
nb['cells'].append(nbf.v4.new_markdown_cell('''## Distribution Analysis

Let's examine the distribution of solar radiation metrics across countries using boxplots.'''))

boxplots = '''# Create boxplots for GHI, DNI, DHI comparison
metrics = ['GHI', 'DNI', 'DHI']
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Solar Radiation Metrics Comparison Across Countries', fontsize=16)

for i, metric in enumerate(metrics):
    sns.boxplot(data=combined_df, x='Country', y=metric, ax=axes[i])
    axes[i].set_title(f'{metric} Distribution')
    axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()'''

nb['cells'].append(nbf.v4.new_code_cell(boxplots))

# Add statistical analysis section
nb['cells'].append(nbf.v4.new_markdown_cell('''## Statistical Analysis

Let's calculate summary statistics and perform statistical tests to compare the metrics across countries.'''))

stats_calc = '''# Calculate summary statistics
summary_stats = combined_df.groupby('Country')[metrics].agg([
    'count', 'mean', 'std', 'min', 'max'
]).round(2)

print("Summary Statistics:")
display(summary_stats)'''

nb['cells'].append(nbf.v4.new_code_cell(stats_calc))

# Add statistical tests
stats_test = '''# Perform Kruskal-Wallis H-test for each metric
print("Statistical Tests (Kruskal-Wallis H-test):")
for metric in metrics:
    h_stat, p_val = stats.kruskal(
        *[df[metric].values for df in dfs]
    )
    print(f"\\n{metric}:")
    print(f"H-statistic: {h_stat:.2f}")
    print(f"p-value: {p_val:.4f}")'''

nb['cells'].append(nbf.v4.new_code_cell(stats_test))

# Add visualization section
nb['cells'].append(nbf.v4.new_markdown_cell('''## Visualization of Mean Values

Let's create a bar plot to compare mean solar radiation values across countries.'''))

viz = '''# Create bar plots for mean values
plt.figure(figsize=(12, 6))
means = combined_df.groupby('Country')[metrics].mean()
means.plot(kind='bar', rot=45)
plt.title('Mean Solar Radiation Values by Country')
plt.ylabel('Radiation (W/m²)')
plt.legend(title='Metric')
plt.tight_layout()
plt.show()

# Save summary statistics to CSV
summary_stats.to_csv('../../data/solar_comparison_summary.csv')
print("\\nSummary statistics saved to 'data/solar_comparison_summary.csv'")'''

nb['cells'].append(nbf.v4.new_code_cell(viz))

# Write the notebook to a file
with open('notebooks/exploratory/compare_countries.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f) 