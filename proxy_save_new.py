from pymongo import MongoClient
from datetime import datetime
# import json

now = datetime.now()
curremtDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

def create_mongo_database():
    #create connection with mongo
    global mongoclient
    global db
    mongoclient = MongoClient('localhost', 27017)
    #create database if not exist
    # db = mongoclient['youtube_viewer']
    db = mongoclient['demoDB']

def create_collection_mongo(collectionName):
    global mongoclient
    global mycol
    global db
    # print("create table/collection in mongo")
    mycol = db[collectionName]

def update_data_to_mongo(data,collectionName,type):
    create_collection_mongo(collectionName)
    if type == "single":
        insert_one_record(data)
    else:
        insert_many_record(data)

def insert_one_record(insertObj):
    global mycol
    print("insert into mongo code here")
    mycol.insert_one(insertObj)

def insert_many_record(insertObj):
    global mycol
    print("insert multiple data in mongo code here")
    mycol.insert_many(insertObj)

def update_record():
    global mycol
    
def find_all_data():
    print("find all data")
    for x in mycol.find():
        print(x)




create_mongo_database()
# myquery = {"proxy_url":"209.205.212.34","proxy_port":1201}
create_collection_mongo("proxy_master_new")
# find_all_data()
# resultData = mycol.find_one(myquery)
# print(resultData)
# y = json.loads(resultData)
'''
if(resultData):
    if "proxy_master_id" in resultData:
        print("key available")
        print(resultData["_id"])
    else:
        print('key not found!')
else:
    print("test")
exit()
'''
# for rdata in resultData:
#     print(rdata["proxy_master_id"])
# print(resultData)

# print(db.list_collection_names())
# exit()
create_collection_mongo("proxy_master_new")
mycol.drop()
# exit()
for x in range(500):
    port = 10000 + x
    y = 100
    # myquery = { "proxy_url":"73.127.11.108","proxy_port":port }
    create_collection_mongo("proxy_master_new")
    # resultData = mycol.find(myquery)
    # if (mycol.find(myquery)):
    #     print("data with port available =>",port)
    # else:
    proxy_master_id = x + y + 1
    proxy_master_data = {
        "proxy_master_id":proxy_master_id,
        "proxy_url":"209.205.197.90",
        "proxy_port":port,
        "username":"ryanturner-country-US",
        "password":"9d60c3-eb6dc2-49ca5d-0f16ca-6a2bb1",
        "created_date":curremtDateTime,
        "modified_date":curremtDateTime
    }
    update_data_to_mongo(proxy_master_data,"proxy_master_new","single")

# for x in mycol.find(myquery):
#     print(x)