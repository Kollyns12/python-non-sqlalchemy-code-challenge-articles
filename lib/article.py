class Article:
    all = []

    def __init__(self, author, magazine, title):
        from lib.author import Author
        from lib.magazine import Magazine

        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.author import Author
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.magazine import Magazine
        if isinstance(value, Magazine):
            self._magazine = value
