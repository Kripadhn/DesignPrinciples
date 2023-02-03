Interface Segregation Principle (ISP) - Clients should not be forced to depend on interfaces they do not use.
Example: A class that implements a simple document with open and save operations, and a separate interface for printing operations.

class OpenableDocument:
    def open(self):
        # code to open the document
        pass

class SaveableDocument:
    def save(self):
        # code to save the document
        pass

class SimpleDocument(OpenableDocument, SaveableDocument):
    pass

simple_doc = SimpleDocument()
simple_doc.open() # Works fine
simple_doc.save() # Works fine
