Dependency Inversion Principle (DIP) - High-level modules should not depend on low-level modules. Both should depend on abstractions.
Example: A class that implements a frontend for a data storage system, and a class that implements the backend for the data storage system.

class DataStore:
    def save_data(self, data):
        # code to save data to the data store
        pass

class Backend:
    def __init__(self, data_store):
        self.data_store = data_store

    def save_data(self, data):
        self.data_store.save_data(data)

class Frontend:
    def __init__(self, backend):
        self.backend = backend

    def save_data(self, data):
        self.backend.save_data(data)
