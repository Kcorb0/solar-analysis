import csv
import codecs
import urllib.request
import urllib.error
import ssl
import sys

BASEURL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
APIKEY = ""
UNITGROUP = "metric"
FILETYPE = "csv"
INTERVAL = "days"


def file_ingestion(loc, startdate="", enddate=""):

    location = str(loc)
    api_query = BASEURL + location

    if len(UNITGROUP):
        api_query += "&unitGroup=" + UNITGROUP

    if len(FILETYPE):
        api_query += "&contentType=" + FILETYPE

    if len(INTERVAL):
        api_query += "&include=" + INTERVAL

    api_query += "&key=" + APIKEY

    print(f"running query for ({api_query})")

    gcontext = ssl.SSLContext()
    info = urllib.request.urlopen(api_query, context=gcontext)
    return info
    # Replace with some kind of regex to decide if its a postcode

    # Check if information already exists in database

    # if len(addr) > 7:
    #    return None
    # else:
    #    return None


if __name__ == "__main__":
    location = "London"
    address_full = "46 Victoria Riverside, Leeds"
    file_ingestion(loc=location)
