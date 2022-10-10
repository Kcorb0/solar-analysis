from cgi import test
import pyodbc
from config import conn

cursor = conn.cursor()

test_q = """
    SELECT TOP (1) * FROM locationdata_full
"""


cursor.execute(test_q)

for i in cursor:
    print(i)
