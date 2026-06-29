from news_lk3.core import AbstractNewsPaper


class SiyathafmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.siyathafm.lk/',
        ]
