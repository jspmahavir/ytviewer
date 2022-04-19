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
    # print("create table/collection in mongo")
    mycol = db[collectionName]

def update_record():
    global mycol


def update_collection_record(collectionName, filter, updateObj):
    global mongoclient
    global db
    tmpCollection = db[collectionName]
    newvalues = { "$set": updateObj }
    tmpCollection.update_one(filter, newvalues)
    print('collection updated')

def copy_collection_record(oldCollection, newCollection, filter):
    global mongoclient
    global db
    tmpCollectionOld = db[oldCollection]
    tmpCollectionNew = db[newCollection]
    tmpArr = tmpCollectionOld.find(filter, { "_id": 0})
    for record in tmpArr:
        tmpCollectionNew.insert_one(record)
        tmpCollectionOld.delete_one(filter)
    print('collection copied')

proxy = 'ryanturner-country-US:9d60c3-eb6dc2-49ca5d-0f16ca-6a2bb1@209.205.197.90:10134'

create_mongo_database()

filter = { 'proxy': proxy }

'''
updateData = {
    'status':200
}
'''

# update_collection_record("youtube_stats", filter, updateData)
copy_collection_record("youtube_stats","youtube_stats_master", filter)