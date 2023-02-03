class Document:
    def open(self):
        pass

    def save(self):
        pass

    def print(self):
        pass

class OpenableDocument(Document):
    def open(self):
        # code to open the document
        pass

class SaveableDocument(Document):
    def save(self):
        # code to save the document
        pass

class SimpleDocument(OpenableDocument, SaveableDocument):
    pass

simple_doc = SimpleDocument()
simple_doc.open() # Works fine
simple_doc.save() # Works fine
simple_doc.print() # AttributeError: 'SimpleDocument' object has no attribute 'print'


