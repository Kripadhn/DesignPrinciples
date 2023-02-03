Solution:
class Database:
def save_data(self, data):
# code to save data to the database

class Backend:
def init(self, database):
self.database = database

def save_data(self, data):
    self.database.save_data(data)
class Frontend:
def init(self, backend):
self.backend = backend
database = Database()
backend = Backend(database)
frontend = Frontend(backend)
frontend.save_data("data") # Works fine