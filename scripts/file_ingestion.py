import csv
import codecs
import urllib.request
import urllib.error
import ssl
import sys
from config import APIKEY


BASEURL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
UNITGROUP = "metric"
FILETYPE = "csv"
INTERVAL = "days"

# Returns the request data from the visualcrossing api based
# on the location and optional start / end dates
# Note: No start/end date will return the forecast
def get_files(loc, startdate="", enddate=""):

    location = str(loc)
    api_query = BASEURL + location + "?"

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


# Used to parse the output data from the api call
# to a csv format.
def file_ingestion(file, slocal=False):
    csv_text = csv.reader(codecs.iterdecode(file, "utf-8"))

    return csv_text


if __name__ == "__main__":
    location = "Huddersfield"
    output = get_files(loc=location)
    csv_data = file_ingestion(output)

    path = f"C:/Users/Josh/Desktop/{location}.csv"
    with open(path, "w") as f:
        writer = csv.writer(f)

        for i in csv_data:
            writer.writerow(i)

        print(f"Output created for {location}.csv")
