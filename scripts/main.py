from json import load
from file_ingestion import get_files, convert_to_csv
from load_in_database import load_in_database

if __name__ == "__main__":

    ### Extract
    location = input("Provide location: ")
    files = get_files(location, startdate="2021-01-01", enddate="2021-12-31")

    ### Transform
    csv_converted = convert_to_csv(files)

    ### Load
    load_in_database(csv_converted)
