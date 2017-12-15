from database.database import Database
import uuid

class Image(object):
    def __init__(self, image, _id=None):
        self.image = image
        self._id = uuid.uuid4().hex if _id is None else _id
    
    @staticmethod
    def save_to_mongo(image, content_type, filename, label):
        Database.insert_image('images', image, content_type, filename, label)
        
    
    @classmethod
    def get_images(cls):
        images = Database.get_images('images')
        return [cls(**image) for image in images]

    
