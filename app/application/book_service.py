class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, book):
        return self.storage.add(book)

    def delete(self, id):
        self.storage.delete(id)

    def update(self, id, data):
        self.storage.update(id, data)

    def get(self):
        return self.storage.get()
