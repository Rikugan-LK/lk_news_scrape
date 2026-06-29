from news_lk3.core import AbstractNewsPaper


class DeranaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.derana.lk/',
        ]
