class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self._author = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            print("Title must be a string")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            print("Author must be a string")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
