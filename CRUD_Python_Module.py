# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
    
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(
            host=HOST,
            port=PORT,
            username=USER,
            password=PASS,
            authSource='admin'
        )
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

        # Create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None and isinstance(data, dict):
                self.collection.insert_one(data)
                return True
            else:
                return False
        except Exception as e:
            print("An error occurred while inserting the document:", e)
            return False

    # Read method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is not None and isinstance(query, dict):
                results = self.collection.find(query)
                return list(results)
            else:
                return []
        except Exception as e:
            print("An error occurred while reading documents:", e)
            return []
        # Update method to implement the U in CRUD.
    def update(self, query, new_data):
        try:
            if query is not None and isinstance(query, dict):
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                return result.modified_count
            else:
                return 0
        except Exception as e:
            print("An error occurred while updating documents:", e)
            return 0
        
            # Delete method to implement the D in CRUD.
    def delete(self, query):
        try:
            if query is not None and isinstance(query, dict):
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0
        except Exception as e:
            print("An error occurred while deleting documents:", e)
            return 0