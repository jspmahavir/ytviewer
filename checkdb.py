from pymongo import MongoClient

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
    print("create table/collection in mongo")
    mycol = db[collectionName]

def insert_one_record(insertObj):
    global mycol
    print("insert into mongo code here")
    # mycol.insert_one(insertObj)
    for x in mycol.find():
        print(x)

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['demoDB']

proxyCollection = db['proxy_master']
apiCollection = db['api_authentication']

proxyData = proxyCollection.find({"proxy_port":"1201"})
print(proxyData)

print(apiCollection)
exit()

print(coll.find_one("Mahavir"))
exit()

'''

create_mongo_database()
create_collection_mongo("api_authentication")
mydata = { "authentication_id": 1, "client_name": "Nimesh","api_key":"1234567890","whitelisted_server_ip":"192.168.1.35","ytview_support":1,"ytcomment_support":1,"ytlike_support":1,"ytsubscribe_support":1,"created_date":"2021-12-08 11:15:10","modified_date":"2021-12-08 11:15:10"}
insert_one_record(mydata)

'''