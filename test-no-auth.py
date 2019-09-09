import pymongo

client = pymongo.MongoClient(
    "database-no-auth",
    27017,
    replicaset="set",
    connect=False,
)

client.admin.command('ismaster')
