import datetime
import random
import SNMPfile
from MongoDBFile import DatabaseConn
from pysnmp import hlapi
from datetime import datetime

db_collections = {
    "timestamp": "timestampDB",
    "cpu": "Cpu_usageDB",
    "random": "RandomNumbDB"
}
oids = {
    "runtime": "1.3.6.1.2.1.1.3.0",
    "cpu": "1.3.6.1.4.1.9.2.1.56.0"
}

comm = hlapi.CommunityData('cisco')


class Manager:
    #Gets Current time
    def get_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #Inserts into db Through DBMIB
    def insert_into_db(self, db, query):
        db.insert_one_into_db(query)
        return query

    #Gets Runtime of the current connected router
    def get_runtime(self):
        _runtime = SNMPfile.get('192.168.1.1', [oids['runtime']], comm)
        _runtime_query = {"Run": _runtime[oids['runtime']], "Timestamp": self.get_time()}
        return self.insert_into_db(DatabaseConn(db_collections['timestamp']), _runtime_query)

    #Gets usage of the CPU on the router in %
    def get_cpu_usage(self):
        _cpu = SNMPfile.get('192.168.1.1', [oids['cpu']], comm)
        _cpu_usage_query = {"Cpu_usage": _cpu[oids['cpu']], "Timestamp": self.get_time()}
        return self.insert_into_db(DatabaseConn(db_collections['cpu']), _cpu_usage_query)

    #Method for generatinf random data to the database, while i was sick at home
    def generate_random_data_to_db(self):
        _rand = random.randint(10,100)
        _random_query = {"Random": _rand, "Timestamp": self.get_time()}
        return self.insert_into_db(DatabaseConn(db_collections['random']), _random_query)
