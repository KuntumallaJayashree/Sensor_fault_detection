import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self,database_name = DATABASE_NAME)-> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://jayashree123:Jashvik0104@cluster0.ico5gmt.mongodb.net/?retryWrites=true&w=majority"
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                #if mongo_db_url is None:
                #    raise Exception("Environment variable MONGODB_URL_KEY is not set ")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client =  MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name  = database_name
        except Exception as e:
            #raise SensorException(e,sys)
            raise e


