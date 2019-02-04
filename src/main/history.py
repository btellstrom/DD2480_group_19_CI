import pymongo

"""
A class for storing the history of the CI-server. The history is stored 
on a mongoDB as documents.
"""
class History:
    """
    Constructor for the history class
    
    + mongo_name - The name of the database we have the history in
    + mongo_ip - The ip of the mongo database to which we wish to connect
    + mongo_port - The port of the mongoDB
    + mongo_user - The username that is to connect to the mongoDB
    + mongo_pass - The password to the above user
    """
    def __init__(self, mongo_name,
                 mongo_ip,
                 mongo_port,
                 mongo_user,
                 mongo_pass):

        self.mongo_client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (mongo_user,
                                       mongo_pass,
                                       mongo_ip,
                                       mongo_port))
        
        self.db = mongo_client[mongo_name]
        
    """
    Inserts a document into the history

    + document - The document to be inserted
    """
    def insert(document):
        builds = db.builds
        builds.insert_one(document)

    """
    Fetch a number of the latest documents to be added to the history
    
    + n - The number of documents to fetch
    """
    def fetch_n_last(n):
        documents = db.builds.find().skip(db.builds.count() - n)

    """
    Static method to create a document that can be inserted into the 
    mongoDB.
    
    + build_id - The id-number of the build, an integer
    + date_rec - The date when CI-server received the build
    + date_end - The date when the CI-server finished the build
    + status - Specifies whether the build failed or passed
    """
    @staticmethod
    def serialize(build_id, date_rec, date_end, status):
        document = {"buildID": build_id,
                    "dateReceivedBuild": date_rec,
                    "dateFinishedBuild": date_end,                    
                    "status": status}
        
        return document


