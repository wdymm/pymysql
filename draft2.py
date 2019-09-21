# # This file contains functions to combine data from different sources together.

# import pandas as pd
# import QUANTAXIS as qa
# import pymongo
# import json
# import datetime


# def readdata(code, start, end):
#     '''This function loads data from local mongodb using qafetch function from quantaxis.
#         Args:
#             code: stock code, string type.
#             start: start date.
#             end: end date.
#         Returns:
#             A data frame indexed with standard datetime index.
#     '''
#     data = qa.QA_fetch_stock_day_adv(code=code, start=start, end=end)
#     result = data.data
#     result = result.sort_index(ascending=False)
#     result = result.reset_index(level=1)
#     result = result.drop(columns='code')

#     return result


# def get_dtindex(start, end):
#     dtindex = pd.date_range(start=start,
#                             end=end,
#                             freq='D')
#     return dtindex


# def get_parameters(code, start, end):
#     outcome = readdata(code=code, start=start, end=end)
#     dtindex = get_dtindex(start=start, end=end)
#     return outcome, dtindex


# def upload_data(code, start, end):
#     outcome, dtindex = get_parameters(code=code, start=start, end=end)
#     # connect to mongodb
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     database = myclient['mydatabase']
#     datacol = database[code + str(datetime.date.today())]
#     dtindexcol = database[code + str(datetime.date.today()) + 'index']
#     outcome['date'] = outcome.index

#     # datacol.insert(json.loads(outcome.T.to_json()).values())
#     # dtindexcol.insert(json.loads(outcome.T.to_json()).values())
#     return outcome


# def QA_util_to_json_from_pandas(data):
#     """需要对于datetime 和date 进行转换, 以免直接被变成了时间戳"""
#     # if 'datetime' in data.columns:
#     #     data.datetime = data.datetime.apply(str)
#     if 'date' in data.columns:
#         data.date = data.date.apply(str)
#     return json.loads(data.to_json(orient='records'))
#     # return data


# code = '000002'
# start = '2009-07-13'
# end = '2019-07-12'

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# database = myclient['mydatabase']
# datacol = database[code + str(datetime.date.today())]

# dtindex = pd.date_range(start=start, end=end, freq='D')
# outcome = upload_data(code=code, start=start, end=end)
# outcome = QA_util_to_json_from_pandas(outcome)
# # print(outcome)
# datacol.insert_many(outcome)
# # result = json.loads(outcome.to_json(orient='records'))
# # result = result.decode(encoding='utf-8')
# # print(result)
# # result2 = json.loads(result)
# # print(result2)


# from QUANTAXIS.TSBoosting.TSBoosting import TS_Boosting_predict
# start = '2007-10-18'
# end = '2019-08-18'
# by = 'D'
# TS_Boosting_predict(start=start, end=end, by=by, databaseid='mydatabase', collectionid='rawdatatest')


# import os
# import pymongo
# from bson.json_util import dumps

# client = pymongo.MongoClient("mongodb://10.0.75.1:27017/")
# change_stream = client.mydatabase.rawdatatest.watch()
# for change in change_stream:
# import time
# import subprocess


# def run_sleep(period):
#     proc = subprocess.Popen(['timeout', '/t', str(period)])
#     return proc


# start = time.time()
# procs = []
# for _ in range(2):
#     print('start')
#     proc = run_sleep(1)
#     print('end')
#     procs.append(proc)
#     print(proc)
# for proc in procs:
#     proc.communicate()
# end = time.time()
# print(end - start)


from datetime import datetime
import pandas as pd
# timestamp = 42000
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)
data = pd.read_csv('C:/Users/shixu/Downloads/trace_201708/container_usage.csv',
                   index_col=0, header=None)
print(data.head())
outcome1 = data.iloc[:2]
outcome2 = data.iloc[:3]
outcome1.index.names = ['datetime']
outcome1.rename(columns={1: 'y'})
outcome2.index.names = ['datetime']
outcome2.rename(columns={1: 'y'})
# outcome1['datetime'] = pd.to_datetime(outcome1['datetime'])
# outcome2['datetime'] = pd.to_datetime(outcome2['datetime'])

print(outcome1)
print(outcome2)
