import pymongo

from src.api.actions.postgres import add_database

myclient = pymongo.MongoClient("mongodb://nraboy:password1234@localhost:27017/")
def create_db(db_name: str, username: str):
    mydb = myclient["matmon15-" + db_name]
    mycollection = mydb["my_collection"]

    # Insert a document to finalize the database and collection creation
    document = {"name": "Test Document", "value": 1}
    mycollection.insert_one(document)
    return add_database(db_name, username)


