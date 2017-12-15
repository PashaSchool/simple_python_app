import pymongo
from gridfs import GridFS

class Database(object):
    URI = "mongodb://localhost:27017"
    DATABASE = None
    FS = None

    def initialize():
        db = pymongo.MongoClient(Database.URI)
        Database.DATABASE = db['gallery']
        Database.FS = GridFS(Database.DATABASE)


    # @staticmethod
    # def insert(collection, data):
    #     Database.DATABASE[collection].insert(data)

    # @staticmethod
    # def find_all(collection):
    #     return Database.DATABASE[collection].find({})

    @classmethod
    def get_images(cls):
        data = Database.DATABASE['images'].find()
        return data

    @staticmethod
    def save_to_mongo(img, content_type, filename):
        fields = Database.FS.put(img, content_type=content_type, filename=filename)
        # Database.DATABASE['images'].insert({"filename": str(filename), "fields": fields})
         
