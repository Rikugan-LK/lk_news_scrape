from news_lk3.core import AbstractNewsPaper


class MawbimaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.mawbima.lk/',
        ]
