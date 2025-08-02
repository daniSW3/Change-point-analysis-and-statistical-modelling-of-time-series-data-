Business objective  


The main goal of this analysis is to study how important events affect Brent oil prices. This will focus on finding out how changes in oil prices are linked to big events like political decisions, conflicts in oil-producing regions, global economic sanctions, and changes in Organization of the Petroleum Exporting Countries (OPEC) policies. The aim is to provide clear insights that can help investors, analysts, and policymakers understand and react to these price changes better.

Brent Oil Price Analysis - Task 1

Project Overview
This project lays the foundation for analyzing Brent oil price fluctuations using a Bayesian Change Point model. The goal is to define a data analysis workflow, understand the model and data properties, and prepare for detecting structural breaks in the Brent oil price series from May to June 1987. The analysis integrates historical oil market events to hypothesize causes of price changes.
Objectives

Define a clear data analysis workflow.
Compile and structure a dataset of key oil market events.
Analyze time series properties of Brent oil prices.
Explain the purpose and limitations of change point models.

Getting Started
Prerequisites

Python 3.x
Required libraries:
pandas (for data manipulation)
matplotlib (for plotting)
numpy (for calculations)
statsmodels (for stationarity tests)


Install dependencies using:pip install pandas matplotlib numpy statsmodels



Installation

Clone or download the project repository.
Place the following files in the project directory:
BrentOilPrices.csv (sample dataset with Date and Price columns)
oil_market_events.csv (compiled event data with Event Name, Start Date, Description, and Category)


Navigate to the project directory and run the analysis script:python explore_brent_oil_prices.py



Data

BrentOilPrices.csv: Contains daily Brent oil prices from May 20, 1987, to June 26, 1987. Columns include:
Date: Date of price record
Price: Brent oil price in dollars


oil_market_events.csv: Includes 15 key historical oil market events (e.g., 1973 Oil Crisis, 2020 COVID-19 Crash) with approximate start dates, descriptions, and categories (Geopolitical, Economic, OPEC Decisions, Public Health).

Usage

Load and explore the BrentOilPrices.csv data using the provided script.
Visualize price trends and log returns to identify potential change points.
Test for stationarity and document findings.
Review the event data in oil_market_events.csv to align with price changes.

Workflow

Data Collection: Load BrentOilPrices.csv and oil_market_events.csv.
Data Cleaning: Convert dates to datetime format and check for missing values.
Exploratory Data Analysis (EDA): Plot prices, calculate log returns, and assess trends/volatility.
Modeling Preparation: Plan a Bayesian Change Point model using PyMC3.
Interpretation and Communication: Document insights and prepare for a report/dashboard.

Assumptions and Limitations

Assumes the 1987 price data reflects broader market trends.
Limited dataset (38 days) may miss long-term trends or rare events.
Correlation between events and price changes does not imply causation (e.g., other factors like demand shifts may influence prices).

Notes

The script explore_brent_oil_prices.py generates plots and stationarity test results.
Extend the event dataset or price data as needed for comprehensive analysis.
Document all steps and findings in a Jupyter notebook or report for Task 1 deliverables.

License
This project is for educational purposes only. No commercial use intended.
Acknowledgments

Data sourced from historical records (e.g., EIA.gov, OPEC.org, BBC archives).
Inspired by xAI’s guidance on Bayesian Change Point modeling.

Brent Oil Price Analysis - Task 2
Project Overview
This project implements a Bayesian Change Point model to detect structural breaks in Brent oil prices (May-Jun 1987) using PyMC3. It interprets results, associates changes with historical events, and explores advanced extensions for future work. The analysis builds on Task 1’s foundation.
Objectives

Implement a Bayesian Change Point model to identify price shifts.
Interpret model outputs to determine change point dates.
Associate changes with events from oil_market_events.csv.
Quantify impacts and plan advanced analyses.

Getting Started
Prerequisites

Python 3.x

Required libraries:

pandas (data manipulation)
matplotlib (plotting)
numpy (calculations)
statsmodels (stationarity tests)
pymc3 (Bayesian modeling)


Install dependencies:
pip install pandas matplotlib numpy statsmodels pymc3



Installation

Clone or download the project repository.

Place files in the directory:

BrentOilPrices.csv (price data)
oil_market_events.csv (event data)
prepare_data_eda.py (EDA script)
change_point_model.py (model script)


Run scripts in order:
python prepare_data_eda.py
python change_point_model.py



Data

BrentOilPrices.csv: Daily prices from May 20, 1987, to June 26, 1987.
oil_market_events.csv: 15 historical events with dates and categories.

Usage

Run prepare_data_eda.py to visualize prices and log returns.
Run change_point_model.py to fit the change point model.
Analyze trace plots and posteriors to identify change points.
Compare change dates with events and document impacts.

Workflow

Data Preparation: Load and transform price data.
EDA: Plot trends and test stationarity.
Modeling: Define and sample a PyMC3 change point model.
Interpretation: Extract change points and quantify shifts.
Association: Link to events and hypothesize causes.

Assumptions and Limitations

Assumes a single change point; multiple shifts may exist.
Short dataset (38 days) limits reliability of detections.
Correlation with events doesn’t prove causation.

Future Work

Incorporate additional data (e.g., GDP, exchange rates).
Explore VAR or Markov-Switching models for deeper insights.

Notes

Check convergence with pm.plot_trace() and pm.summary().
Document findings in a report or Jupyter notebook.
Adjust model complexity based on data range.

License
Educational use only. No commercial intent.
Acknowledgments

Data from EIA.gov, OPEC.org, and news archives.
Guided by xAI’s Bayesian modeling approach.
