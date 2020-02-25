# ADDRESS TABLE
# imports a bucket
# outputs the list of address lines and associated postcodes

from data7project.scripts.table_scripts.tools.append_tables_buckets import *

def course_schedule(bucket, folder):
    address = Append_All(bucket).append_all(folder)
    # convert all address lines to string
    address["address"] = address["address"].astype(str)
    # convert all address lines to string
    address["postcode"] = address["postcode"].astype(str)
    # strip whitespace in the address string
    address['address'] = address['address'].str.strip()
    # strip whitespace in the address string
    address['postcode'] = address['postcode'].str.strip()
    # if the address starts with a "0" remove this
    address["address"] = address["address"].apply(lambda x: x[1:] if x.startswith("0") else x)

    return address[['address','postcode']]
