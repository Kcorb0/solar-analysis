from django.shortcuts import render
from .models import WeatherData
import csv
import codecs
import urllib.request
import urllib.error
import ssl
import sys


def index(request):
    context = {}
    return render(request, "main/index.html", context)


APIKEY = ""
BASEURL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
UNITGROUP = "metric"
FILETYPE = "csv"
INTERVAL = "days"


def get_files(location, startdate="", enddate=""):

    """
    Returns the request data from the visualcrossing api basedon the location and optional start / end dates.
    Note: No start/end date will return the forecast
    """

    location = str(location)
    api_query = BASEURL + location

    if len(startdate) > 0:
        api_query += "/" + startdate
        if len(enddate) > 0:
            api_query += "/" + enddate

    api_query += "?"

    if len(UNITGROUP) > 0:
        api_query += "&unitGroup=" + UNITGROUP

    if len(FILETYPE) > 0:
        api_query += "&contentType=" + FILETYPE

    if len(INTERVAL) > 0:
        api_query += "&include=" + INTERVAL

    api_query += "&key=" + APIKEY

    print(f"running query for ({api_query})")

    # Try to return the query output, check that the the
    # query is valid.
    try:
        gcontext = ssl.SSLContext()
        info = urllib.request.urlopen(api_query, context=gcontext)
        return info
    except urllib.error.HTTPError as e:
        error_info = e.read().decode()
        print("Error code: ", e.code, error_info)
        sys.exit()
    except urllib.error.URLError as e:
        error_info = e.read().decode()
        print("Error code: ", e.code, error_info)
        sys.exit()


def convert_to_csv(file):
    """
    Parse the output data from an api call to comma seperated values.
    """
    csv_text = csv.reader(codecs.iterdecode(file, "utf-8"))
    return csv_text


def load_in_database(file):

    params = list(file)[1:]

    for x in range(len(params)):
        location = params[x][0].split(", ")[0]
        date = params[x][1].replace("-", "")
        merged_id = location + "_" + date
        params[x].insert(0, merged_id)

    for row in params:
        created = WeatherData.objects.get_or_create(
            namedate_id=row[0],
            name=row[1],
            datetime=row[2],
            tempmax=row[3],
            tempmin=row[4],
            temp=row[5],
            feelslikemax=row[6],
            feelslikemin=row[7],
            feelslike=row[8],
            dew=row[9],
            humidity=row[10],
            precip=row[11],
            precipprob=row[12],
            precipcover=row[13],
            preciptype=row[14],
            snow=row[15],
            snowdepth=row[16],
            windgust=row[17],
            windspeed=row[18],
            winddir=row[19],
            sealevelpressure=row[20],
            cloudcover=row[21],
            visibility=row[22],
            solarradiation=row[23],
            solarenergy=row[24],
            uvindex=row[25],
            severerisk=row[26],
            sunrise=row[27],
            sunset=row[28],
            moonphase=row[29],
            conditions=row[30],
            description=row[31],
            icon=row[32],
            stations=row[33],
        )
        created.save()


def load_main(location):
    loc_data = get_files(location=location)
    csv_data = convert_to_csv(loc_data)
    load_in_database(csv_data)
