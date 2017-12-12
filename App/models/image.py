from database.database import Database

import uuid

class Image(object):
    def __init__(self, image, _id=None):
        self.image = image
        self._id = uuid.uuid4().hex if _id is None else _id
    
    @staticmethod
    def save_to_mongo(image):
        # Database.fs_put(image)
        pass
    
    @classmethod
    def get_images(cls):
        images = Database.find_all('image')
        return [cls(**image) for image in images]
        # return [1,2,3]
    
