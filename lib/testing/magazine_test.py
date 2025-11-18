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
        if not isinstance(value, str) or not (2 <= len(value.strip()) <= 16):
            raise Exception("Name must be 2–16 characters long")
        self._name = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value.strip()

    def articles(self):
        from lib.article import Article
        arts = [a for a in Article.all if a.magazine == self]
        return arts or None

    def contributors(self):
        from lib.article import Article
        arts = [a for a in Article.all if a.magazine == self]
        authors = {a.author for a in arts}
        return list(authors) if authors else None

    def article_titles(self):
        from lib.article import Article
        titles = [a.title for a in Article.all if a.magazine == self]
        return titles or None

    def contributing_authors(self):
        from lib.article import Article
        counts = {}
        for a in Article.all:
            if a.magazine == self:
                counts[a.author] = counts.get(a.author, 0) + 1
        authors = [auth for auth, c in counts.items() if c > 2]
        return authors or None

    @classmethod
    def top_publisher(cls):
        from lib.article import Article
        if not Article.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles() or []), default=None)
