#!/Users/fivesheep/anaconda3/bin/python
# coding: utf-8

from sodapy import Socrata
import numpy as np
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--page_size", '-p', required=True, type=int, help="num of rows returned per query")
parser.add_argument("--num_pages", '-n', type=int, help="num of queries")
parser.add_argument("--output", '-o', help="output file")
args = parser.parse_args()


client = Socrata('data.cityofnewyork.us', '1fIaSdQyO1iFzD4mgU56MCYq5')
dbname = 'nc67-uf89'

num_pages = args.num_pages
page_size = args.page_size
output = args.output

if num_pages is None:
    count = int(client.get(dbname, select='COUNT(*)')[0]['COUNT'])
    num_pages = int(np.ceil(count/page_size))

res = []
for i in range(num_pages):
    res += client.get(dbname, limit=page_size, offset=page_size*i)
if output is not None:
    with open(output, 'w') as f:
        json.dump(res , f)
else:
    print(res)

