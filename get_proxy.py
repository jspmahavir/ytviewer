from pymongo import MongoClient
import json

def create_mongo_database():
    #create connection with mongo
    global mongoclient
    global db
    mongoclient = MongoClient('localhost', 27017)
    #create database if not exist
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
    result = []
    y = ''
    # mydict = create_dict()
    for x in mycol.find():
        # ['baysocial1:69np2nxxm7jb@73.127.11.108:1001',
        y = x['username'] + ':' + x['password'] + '@' + x['proxy_url'] + ':' +str(x["proxy_port"])
        result.append(y)
    return result

create_mongo_database()
create_collection_mongo("proxy_master_new")

resultData = find_all_data()
print("================\n")
# strdata = {"name":"mahavir"}

python_obj = {
  "name": "Mahavir",
  "class":"I",
  "age": 6  
}

print(resultData)
data = json.dumps(resultData)
print("===================\n")
print(data)
print("++++++++++++++++\n")
exit()

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
# create_collection_mongo("proxy_master")
# mycol.drop()
# exit()

'''
for x in range(1000):
    port = 1200 + x
    myquery = { "proxy_url":"209.205.212.34","proxy_port":port }
    create_collection_mongo("proxy_master")
    # resultData = mycol.find(myquery)
    if (mycol.find(myquery)):
        print("data with port available =>",port)
    else:
        proxy_master_id = x + 1
        proxy_master_data = {
            "proxy_master_id":proxy_master_id,
            "proxy_url":"209.205.212.34",
            "proxy_port":port,
            "username":"ryanturner-country-US",
            "password":"9d60c3-eb6dc2-49ca5d-0f16ca-6a2bb1",
            "created_date":curremtDateTime,
            "modified_date":curremtDateTime
        }
        update_data_to_mongo(proxy_master_data,"proxy_master","single")
'''