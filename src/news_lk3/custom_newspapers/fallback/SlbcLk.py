from news_lk3.core import AbstractNewsPaper


class SlbcLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.slbc.lk/',
        ]
