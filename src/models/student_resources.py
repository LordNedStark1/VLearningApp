from models.Book import Book


class Resources:
    def __init__(self, resource_name, date_uploaded):
        self._resource_name = resource_name
        self._book = Book()
        self._date_uploaded = date_uploaded

    def set_resource_name(self, resource_name):
        self._resource_name = resource_name

    def get_resource_name(self):
        return self._resource_name

    def set_book(self, book: Book):
        self._book = book

    def get_book(self):
        return self._book

    def set_date_uploaded(self, date_uploaded):
        self._date_uploaded = date_uploaded

    def get_date_uploaded(self):
        return self._date_uploaded