from news_lk3.core import AbstractNewsPaper


class ShaafmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://www.shaafm.lk/',
        ]
