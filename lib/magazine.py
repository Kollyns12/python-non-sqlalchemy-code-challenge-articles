class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            
            pass

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value
        else:
            
            pass

    def articles(self):
        from lib.article import Article
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        from lib.article import Article
        authors = {a.author for a in Article.all if a.magazine == self}
        return list(authors)

    def article_titles(self):
        from lib.article import Article
        titles = [a.title for a in Article.all if a.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        from lib.article import Article
        counts = {}
        for a in Article.all:
            if a.magazine == self:
                counts[a.author] = counts.get(a.author, 0) + 1
        authors = [auth for auth, count in counts.items() if count > 2]
        return authors if authors else None
