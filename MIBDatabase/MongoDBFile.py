import pymongo
from pymongo import MongoClient


class DatabaseConn:
    def __init__(self, dbname):
        self.conn_string = "mongodb://localhost:27017"
        self.client = MongoClient(self.conn_string)
        self.db = self.client['mongopydb']
        self.db_collection = self.db[dbname]

    def insert_one_into_db(self, data):
        self.db_collection.insert_one(data)

    def insert_array_into_db(self, data_arr):
        for data in data_arr:
            self.db_collection.insert_one(data)

    def get_all_from_db(self):
        return self.db_collection.find()

    def get_sorted_db(self, sort_type, direction):
        return self.db_collection.find().sort(sort_type, direction)
