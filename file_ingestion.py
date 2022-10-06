from nturl2path import url2pathname


def file_ingestion(addr):

    address = str(addr)

    # Replace with some kind of regex to decide if its a postcode

    # Check if information already exists in database

    if len(addr) > 7:
        return None
    else:

        return None


if __name__ == "__main__":
    address_pc = "LS10 1EU"
    address_full = "46 Victoria Riverside, Leeds"
    file_ingestion(address_pc)
