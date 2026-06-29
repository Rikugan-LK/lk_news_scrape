from news_lk3.core import AbstractNewsPaper


class SithafmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://sithafm.lk/',
        ]
