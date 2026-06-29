from news_lk3.core import AbstractNewsPaper


class RupavahiniLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.rupavahini.lk/',
        ]
