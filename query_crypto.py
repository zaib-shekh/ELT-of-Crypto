import sqlite3
import pandas as pd

# 1. Connect to your newly created database
conn = sqlite3.connect("crypto_factory.db")

# 2. WRITE YOUR SQL HERE! (Inside the triple quotes)

my_sql_query = """
SELECT name, current_price, price_change_percentage_24h
FROM crypto_prices
WHERE current_price < 1.0
ORDER BY price_change_percentage_24h DESC
LIMIT 3"""

# 3. Run the SQL and print the results
results = pd.read_sql_query(my_sql_query, conn)
print("=== CRYPTO REPORT ===")
print(results)

conn.close()
