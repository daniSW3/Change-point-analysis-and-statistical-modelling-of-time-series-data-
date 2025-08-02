import pandas as pd

# Define the event data (replace with your researched events)
data = [
    {"Event Name": "1973 Oil Crisis", "Start Date": "1973-10-17", "Description": "OAPEC imposed an oil embargo on nations supporting Israel in the Yom Kippur War, quadrupling oil prices from $3 to $12 per barrel.", "Category": "Geopolitical"},
    {"Event Name": "1979 Iranian Revolution", "Start Date": "1979-01-16", "Description": "The revolution disrupted Iran's oil production, causing a supply shortage and doubling oil prices to over $30 per barrel.", "Category": "Geopolitical"},
    {"Event Name": "1980 Iran-Iraq War", "Start Date": "1980-09-22", "Description": "The war reduced oil output from Iran and Iraq, leading to price spikes and global supply concerns.", "Category": "Geopolitical"},
    {"Event Name": "1986 Oil Glut", "Start Date": "1986-01-01", "Description": "OPEC increased production to regain market share, causing a supply glut and a 50% price drop to around $10 per barrel.", "Category": "OPEC Decisions"},
    {"Event Name": "1990 Gulf War", "Start Date": "1990-08-02", "Description": "Iraq’s invasion of Kuwait disrupted oil supplies, causing prices to double to $40 per barrel before stabilizing.", "Category": "Geopolitical"},
    {"Event Name": "1997 Asian Financial Crisis", "Start Date": "1997-07-01", "Description": "Economic collapse in Asia reduced oil demand, leading to a price drop to below $15 per barrel.", "Category": "Economic"},
    {"Event Name": "2003 Iraq War", "Start Date": "2003-03-20", "Description": "The U.S. invasion of Iraq disrupted oil exports, causing price volatility and a rise to $35 per barrel.", "Category": "Geopolitical"},
    {"Event Name": "2008 Financial Crisis", "Start Date": "2008-09-15", "Description": "Global demand collapsed after Lehman Brothers’ bankruptcy, causing oil prices to plummet from $145 to $32 per barrel.", "Category": "Economic"},
    {"Event Name": "2011 Arab Spring", "Start Date": "2011-02-01", "Description": "Uprisings in Libya and Egypt disrupted oil production, pushing prices above $100 per barrel.", "Category": "Geopolitical"},
    {"Event Name": "2014 OPEC Production Decision", "Start Date": "2014-11-27", "Description": "OPEC maintained production levels despite a supply glut, leading to a price collapse from $110 to below $50 per barrel.", "Category": "OPEC Decisions"},
    {"Event Name": "2016 OPEC+ Production Cut", "Start Date": "2016-11-30", "Description": "OPEC and non-OPEC members agreed to cut production by 1.8 million barrels per day, stabilizing prices around $50 per barrel.", "Category": "OPEC Decisions"},
    {"Event Name": "2020 COVID-19 Crash", "Start Date": "2020-03-01", "Description": "Global demand fell due to the pandemic; a Russia-Saudi price war caused prices to drop to negative levels in April.", "Category": "Public Health"},
    {"Event Name": "2020 Russia-Saudi Price War", "Start Date": "2020-03-08", "Description": "Russia rejected OPEC’s proposed cuts, prompting Saudi Arabia to slash prices, leading to a 65% oil price drop.", "Category": "OPEC Decisions"},
    {"Event Name": "2022 Russia-Ukraine War", "Start Date": "2022-02-24", "Description": "Russia’s invasion and Western sanctions on Russian oil caused prices to spike to $120 per barrel.", "Category": "Geopolitical"},
    {"Event Name": "2023 OPEC+ Production Cut", "Start Date": "2023-04-02", "Description": "OPEC+ announced voluntary cuts of 1.65 million barrels per day, pushing prices to $87 per barrel before declining.", "Category": "OPEC Decisions"}
]


# Create DataFrame
df = pd.DataFrame(data)

# Convert Start Date to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'])

# Validate data
print("Checking for missing values:\n", df.isna().sum())
print("\nData types:\n", df.dtypes)
print("\nPreview:\n", df.head())

# Save to CSV
df.to_csv('oil_market_events.csv', index=False)
print("CSV saved as 'oil_market_events.csv'")