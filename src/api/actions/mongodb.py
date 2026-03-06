import pymongo

from src.api.actions.postgres import add_database, get_database, update_db_name
from src.api.modules.deployment import Dep

myclient = pymongo.MongoClient("mongodb://nraboy:password1234@localhost:27017/")
def create_mongo_db(db_name: str, username: str):
    mydb = myclient["matmon15-" + db_name]
    mycollection = mydb["my_collection"]

    # Insert a document to finalize the database and collection creation
    document = {"name": "Test Document", "value": 1}
    mycollection.insert_one(document)
    return add_database(db_name, username)


def update_mongodb_name(deployment_id: str, dep: Dep):
    old_db_name = get_database(deployment_id).get("db_name")
    old_db =myclient[old_db_name]
    new_db = myclient["matmon15-" + dep.db_name]
    #("setParameter", {"db_name": dep.db_name})
    for col_name in old_db.list_collection_names():
        print(col_name)
        old_coll = old_db[col_name]
        new_coll = new_db[col_name]

        documents = old_coll.find()
        if documents:
            new_coll.insert_many(documents)
    print(old_db_name)
    print(dep.db_name)
    #myclient.drop_database(old_db_name)

    #db = myclient.copyDatabase("old_db_name", dep.db_name, "localhost")
    #db = db.dropDatabase();
    #myclient.admin.command("setParameter", {"db_name": db_name.db_name, "parameter": deployment_id})
    return update_db_name(deployment_id, dep)