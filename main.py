import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')
products_all = pd.read_sql("""
SELECT *
 FROM products;
""", conn)

desc_count = pd.read_sql("""
SELECT productLine, COUNT(*) AS count
    FROM products
    GROUP BY productLine
    ORDER BY count DESC;
""", conn)

grouping_products = pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice
    FROM products
    GROUP BY productLine
    ORDER BY avgPrice DESC;
""", conn)

group_by_min_max = pd.read_sql("""
SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP
 FROM products
 GROUP BY productLine
""", conn)

group_by_where = pd.read_sql("""
SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP
 FROM products
 WHERE MSRP >= 50
 GROUP BY productLine
""", conn)

group_by_having = pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice
 FROM products
 GROUP BY productLine
 HAVING avgPrice >= 50
 ORDER By avgPrice DESC
""", conn)

group_by_where_having = pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice, AVG(MSRP) AS avgMSRP
 FROM products
 WHERE MSRP >= 50
 GROUP BY productLine
 HAVING avgPrice >= 50
 ORDER By avgPrice ASC
""", conn)

conn.close()