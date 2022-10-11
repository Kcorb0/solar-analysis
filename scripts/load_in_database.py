from cgi import test
import pydoc
import pyodbc
from config import conn

cursor = conn.cursor()


def load_in_database(file):

    params = file[1:]

    insert_values = """
        INSERT INTO full_weatherdata(
        namedate_id,
        name,
        datetime,
        tempmax,
        tempmin,
        temp,
        feelslikemax,
        feelslikemin,
        feelslike,
        dew,
        humidity,
        precip,
        precipprob,
        precipcover,
        preciptype,
        snow,
        snowdepth,
        windgust,
        windspeed,
        winddir,
        sealevelpressure,
        cloudcover,
        visibility,
        solarradiation,
        solarenergy,
        uvindex,
        severerisk,
        sunrise,
        sunset,
        moonphase,
        conditions,
        description,
        icon,
        stations
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """

    for x in range(len(params)):
        location = params[x][0].split(", ")[0]
        date = params[x][1].replace("-", "")
        merged_id = location + "_" + date
        params[x].insert(0, merged_id)

    try:
        cursor.executemany(insert_values, params)
    except pyodbc: 
    
    else:
    finally:
