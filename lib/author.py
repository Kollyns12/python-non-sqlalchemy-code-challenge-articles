class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name.strip()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        pass

    
    def articles(self):
        from lib.article import Article
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        from lib.article import Article
        mags = {a.magazine for a in Article.all if a.author == self}
        return list(mags)

    def add_article(self, magazine, title):
        from lib.article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if mags:
            return list({m.category for m in mags})
        return None

