import pymongo

#連線到 MongoDB

from pymongo.mongo_client import MongoClient

uri = "資料庫位置"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#把資料放進資料庫
db=client.website #選擇操作 website 資料庫
collection=db.users # 選擇操作 users 集合
# 把資料新增到集合中
# 一次新增多筆資料的編號
result=collection.insert_many([{
    "name":"bill",
    "email":"bill@gmail.com",
    "password":"xd",
    "level":2
},{
    "name":"Arvin",
    "email":"arvin@gmail.com",
    "password":"aaa",
    "level":3
}])
print("資料新增成功")
print(result.inserted_ids)




# result=collection.insert_one({
#     "name":"bill",
#     "email":"bill@gmail.com",
#     "password":"xd",
#     "level":2
# })


db=client.test #選擇操作 test 資料庫
collection=db.users # 選擇操作 users 集合
# 把資料新增到集合中
collection.insert_one({
    "name":"arvin",
    "gender":"男"
})
print("資料新增成功")
print(result.inserted_id)

#取得集合中第一筆文件資料
data=collection.find_one()
print(data)



from bson.objectid import ObjectId
#根據objectId取得文件資料
data=collection.find_one(
    ObjectId("64a45d73f4b552b0a619161b")
)
print(data)

#取得文件中的欄位
print(data["_id"])
print(data["email"])


#一次取得多筆文件資料
cursor=collection.find()
print(cursor)
for doc in cursor:
    print(doc["name"])


# #更新集合中的一筆文件資料
result=collection.update_one({
    "email":"arvin@gmail.com"
},{"$set":{
    "description":"I'm arvin"
}
})

#資料+5
# result=collection.update_one({
#     "email":"arvin@gmail.com"
# },{"$inc":{  
#     "level":5
# }
# })


#資料/5
# result=collection.update_one({
#     "email":"arvin@gmail.com"
# },{"$mul":{  
#     "level":0.5
# }
# })



# #拿掉欄位
result=collection.update_one({
    "email":"arvin@gmail.com"
},{"$unset":{
    "description":""
}
})

#更新集合中的多筆文件資料

result=collection.update_many({
    "level":2},{
    "$set":{
        "level":4
        } 
    })


# print("符合篩選條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)

#刪除文件中的一筆資料
result=collection.delete_one({
    "email":"arvin@gmail.com"
})
print("實際刪除的資料:",result.deleted_count)

#刪除文件中的多筆資料
result=collection.delete_many({
    "level":5
})
print("實際刪除的資料:",result.deleted_count)




#複合篩選條件 and跟or
doc=collection.find_one({"$and":[
    {"email":"arvin@gmail.com"},
    {"password":"aaa"}]
})
print("取得的資料",doc)

#篩選結果排序
cur=collection.find({
    "$or":[{
        "email":"arvin@gmail.com"},
        {"level":4}
        ]
},sort=[
    ("level",pymongo.ASCENDING)
])
for doc in cur:
    print(doc)