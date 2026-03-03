import requests
import pandas as pd
import sqlite3

print("Starting the Python Delivery Truck...")

# ==========================================
# 1. EXTRACT: Go to the internet and get the data
# ==========================================
print("Fetching live data from CoinGecko API...")
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1"
response = requests.get(url)
raw_data = response.json()

# ==========================================
# 2. TRANSFORM: Clean it up using Pandas
# ==========================================
print("Cleaning and organizing the data...")
df = pd.DataFrame(raw_data)

# We only want to keep the important columns for our SQL analysis later
clean_df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]

# ==========================================
# 3. LOAD: Dump it into our local SQL Database
# ==========================================
print("Loading data into local SQLite database...")
# This creates a file called 'crypto_factory.db' in your folder
connect = sqlite3.connect('crypto_factory.db')

# Dump our clean Pandas data directly into a SQL table called 'crypto_prices'
clean_df.to_sql('crypto_prices', connect, if_exists='replace', index=False)
connect.close()

print("SUCCESS! Pipeline complete. Data is ready for SQL.")