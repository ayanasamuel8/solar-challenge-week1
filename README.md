# Solar Challenge Week 1

This repository contains the code and resources for the Solar Challenge Week 1 project.

## Project Structure

```
├── .vscode/              # VS Code settings
├── .github/              # GitHub Actions workflows
├── src/                  # Source code
├── notebooks/            # Jupyter notebooks
├── tests/               # Unit tests
└── scripts/             # Utility scripts
```

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd solar-challenge-week1
```

2. Create and activate a virtual environment:

For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

For Unix/MacOS:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Development

- Code formatting is handled by `black`
- Linting is done with `pylint`
- Tests are written using `pytest`

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## License


## Exploratory Data Analysis (EDA)

The EDA was performed for three countries: **Benin (Malanville)**, **Sierra Leone (Bumbuna)**, and **Togo (Dapaong)**. The analysis included:

- **Data Loading & Cleaning:**
	- Datasets were loaded and timestamps parsed.
	- Outliers were detected using Z-scores (|Z| > 3) for key variables (GHI, DNI, DHI, ModA, ModB, WS, WSgust).
	- Missing values in critical columns (GHI, DNI, DHI, Tamb) were imputed with the median.
	- Cleaned datasets were prepared for further analysis.

- **Descriptive Statistics & Missing Data:**
	- Summary statistics were generated for each country’s key performance indicators.
	- Missing data percentages were reported, highlighting any columns with >5% missingness.

- **Visualizations:**
	- Time series plots of solar irradiance (GHI, DNI, DHI) for January 2023.
	- Bar plots showing the impact of cleaning on module performance (ModA).
	- Correlation heatmaps for financial and risk variables (GHI, DNI, DHI, Tamb, TModA, RH, WS).

### Country Highlights

#### Benin (Malanville)
- Data showed typical seasonal and daily solar patterns.
- Outliers and missing values were handled as described above.
- Cleaning activities had a measurable positive impact on module output.
- Correlation analysis revealed strong relationships between irradiance and module performance.

#### Sierra Leone (Bumbuna)
- Similar EDA steps as Benin.
- Some differences in missing data patterns and outlier frequency.
- Cleaning and correlation patterns were consistent with Benin, with some site-specific variations.

#### Togo (Dapaong)
- EDA followed the same process.
- Data quality and trends were comparable to the other sites.
- Cleaning and correlation analyses provided actionable insights for site management.

For detailed code and plots, see the [notebooks/eda.ipynb](notebooks/eda.ipynb).

[MIT License](LICENSE)
