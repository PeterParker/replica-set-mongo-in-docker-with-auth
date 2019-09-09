import pymongo

client = pymongo.MongoClient(
    "database-auth",
    27017,
    replicaset="set",
    connect=False,
    username="user",
    password="pass",
)

client.admin.command('ismaster')
