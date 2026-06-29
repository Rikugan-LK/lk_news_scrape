from news_lk3.core import AbstractNewsPaper


class LmdLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lmd.lk/',
        ]
