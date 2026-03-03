# 🚀 Crypto ELT Pipeline: Local Data Engineering Factory

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=flat&logo=sqlite)
![Pandas](https://img.shields.io/badge/Pandas-Data_Cleaning-darkblue?style=flat&logo=pandas)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?style=flat)

## 📖 Project Overview
This project is a lightweight, fully functional Data Engineering pipeline (ELT) built from scratch. It extracts live cryptocurrency market data, loads it into a local relational database, and uses SQL to transform and analyze the data to find actionable investment insights.

## 🏗️ Architecture & Workflow

1. **Extract (API Integration):** Uses Python (`requests`) to connect to the live CoinGecko API and fetch the top 50 cryptocurrencies by market cap in JSON format.
2. **Load (Local Data Warehouse):** Cleans and structures the raw JSON data using `pandas`, then loads it directly into a local `SQLite` database (`crypto_factory.db`).
3. **Transform & Analyze (SQL):** Uses standard SQL queries to filter, sort, and aggregate the database. For example: finding the top-performing "penny cryptos" (coins under $1.00) based on 24-hour price changes.

## 🗂️ Files in this Repository
* `ELT_Using_Pandas_SQlite3.py`: The main ELT script that acts as the "delivery truck," fetching the API data and building the database.
* `query_crypto.py`: The analytics script that connects to the database and runs SQL queries to print insights to the terminal.

## 🚀 How to Run It Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/zaib-shekh/ELT-of-Crypto.git](https://github.com/zaib-shekh/ELT-of-Crypto.git)
cd ELT-of-Crypto
2. Install the required Python libraries:

Bash
pip install requests pandas
3. Run the pipeline to build your database:

Bash
python ELT_Using_Pandas_SQlite3.py
4. Run the SQL queries to see the data:

Bash
python query_crypto.py
📊 Sample SQL Insight
Here is an example of the SQL used to find the top 3 trending cheap coins (under $1):

SQL
SELECT name, current_price, price_change_percentage_24h
FROM crypto_prices
WHERE current_price < 1.0
ORDER BY price_change_percentage_24h DESC
LIMIT 3;

---

### 🚀 Step 2: Push it all to GitHub!

Now that you have your `README.md`, your `ELT_Using_Pandas_SQlite3.py`, and your `query_crypto.py` all sitting in your folder, let's push the entire package up to GitHub.

Run these exact commands in your VS Code terminal:

**1. Add all three files:**
```bash
git add README.md ELT_Using_Pandas_SQlite3.py query_crypto.py
2. Save the snapshot:

Bash
git commit -m "Complete portfolio project: Added Python scripts and README"
3. Push to the cloud:

Bash
git push -u origin main
