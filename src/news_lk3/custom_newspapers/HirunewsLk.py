from news_lk3.core import AbstractNewsPaper


class HirunewsLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.hirunews.lk/',
        ]
