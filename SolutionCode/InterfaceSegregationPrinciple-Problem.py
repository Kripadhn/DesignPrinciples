class Document:
    def open(self):
        pass

    def save(self):
        pass

    def print(self):
        pass

class SimpleDocument(Document):
    def save(self):
        # code to save the document
        pass

simple_doc = SimpleDocument()
simple_doc.open() # AttributeError: 'SimpleDocument' object has no attribute 'open'
