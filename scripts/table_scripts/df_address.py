# import the pullcsv tool
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from fuzzywuzzy import fuzz
address = PullCsv("data7-engineering-project").pull("Talent", "April2019Applicants.csv")

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

print(address[['address','postcode']])