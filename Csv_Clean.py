import boto3
import pprint as pp
import json
import numpy as np
import pandas as pd
import csv
import re

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

print(s3_client)
print(s3_resource)

## pp.pprint(s3_client.list_buckets()['Buckets'])  # this

contents = s3_client.list_objects(Bucket='data7-engineering-project')
# pp.pprint(contents['Contents'])

# for key in contents['Contents']:
#     print(key['Key'])



s3object = s3_client.get_object(Bucket='data7-engineering-project',
                                Key='Academy/Business_24_2019-02-11.csv')
# pp.pprint(s3object)

strbody = s3object['Body'].read()

pp.pprint(strbody)

contents = s3_client.list_objects(Bucket='data7-engineering-project')

pd.read_csv(strbody.decode('utf-8'), sep=',', header=None)

# class excel where i pull the csv file
# clean the data and push it back on the cloud

# orig = b'settlement-id\tsettlement-start-date\tsettlement-end-date\tdeposit-date\ttotal-amount\tcurrency\ttransaction-type\torder-id\tmerchant-order-id\tadjustment-id\tshipment-id\tmarketplace-name\tamount-type\tamount-description\tamount\tfulfillment-id\tposted-date\tposted-date-time\torder-item-code\tmerchant-order-item-id\tmerchant-adjustment-item-id\tsku\tquantity-purchased\n7293436482\t03.05.2018 09:10:07 UTC\t04.05.2018 20:30:23 UTC\t06.05.2018 20:30:23 UTC\t53,44\tEUR\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n7293436482\t\t\t\t\t\tOrder\t303-3746292-6119509\t\t\tDRGC8lFbB\tAmazon.de\tItemPrice\tPrincipal\t179,99\tMFN\t03.05.2018\t03.05.2018 17:12:22 UTC\t30407746733299\t\t\t3700546702556-180412-chp-18c10347-1\t1\n7293436482\t\t\t\t\t\tOrder\t303-3746292-6119509\t\t\tDRGC8lFbB\tAmazon.de\tItemFees\tCommission\t-32,40\tMFN\t03.05.2018\t03.05.2018 17:12:22 UTC\t30407746733299\t\t\t3700546702556-180412-chp-18c10347-1\t1\n7293436482\t\t\t\t\t\tRefund\t305-1251749-5602732\t305-1251749-5602732\tamzn1:crow:YZkTuxs4RhO8FpZez3cGCg\t\tAmazon.de\tItemPrice\tPrincipal\t-109,99\tAFN\t04.05.2018\t04.05.2018 18:24:39 UTC\t38048998219979\t\t142721169810\t3700546702082-180124-jpn-131N28-6\t\n7293436482\t\t\t\t\t\tRefund\t305-1251749-5602732\t305-1251749-5602732\tamzn1:crow:YZkTuxs4RhO8FpZez3cGCg\t\tAmazon.de\tItemFees\tCommission\t19,80\tAFN\t04.05.2018\t04.05.2018 18:24:39 UTC\t38048998219979\t\t142721169810\t3700546702082-180124-jpn-131N28-6\t\n7293436482\t\t\t\t\t\tRefund\t305-1251749-5602732\t305-1251749-5602732\tamzn1:crow:YZkTuxs4RhO8FpZez3cGCg\t\tAmazon.de\tItemFees\tRefundCommission\t-3,96\tAFN\t04.05.2018\t04.05.2018 18:24:39 UTC\t38048998219979\t\t142721169810\t3700546702082-180124-jpn-131N28-6\t\n'



