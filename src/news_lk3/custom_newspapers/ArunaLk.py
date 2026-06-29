from news_lk3.core import AbstractNewsPaper


class ArunaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.aruna.lk/',
        ]
