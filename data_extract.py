import sqlite3

# Initialize serverless database and cursor to use PostgreSQL queries
connection = sqlite3.connect("solarweather.db")
curs = connection.cursor()

# Create table
curs.execute(
    """
CREATE TABLE weather(
    name, 
    datetime, 
    tempmax, 
    tempmin, 
    temp,
    dew,
    humidity,
    precip,
    precipcover,
    preciptype,
    snowdept,
    windspeed,
    cloudcover,
    visibility,
    solarradiation,
    solarenergy,
    uvindex,
    severerisk,
    sunrise,
    sunset,
    moonphase
)
"""
)
