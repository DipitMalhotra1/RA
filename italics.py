import sys
import pandas as pd
import pymongo
import json
import os


def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['sql2md']
    collection_name = 'new'
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json,check_keys=False)

if __name__ == "__main__":
  filepath = '/path/to/csv/path'
  import_content("/Users/dipit/Documents/RA/RA/sample1.csv")