import sqlite3 as sql

sql_db = sql.connect("15.0.2000.5")


print(
    sql_db.cursor(
        """
USE SQLCookbookSB;

SELECT * FROM debt;
"""
    )
)
