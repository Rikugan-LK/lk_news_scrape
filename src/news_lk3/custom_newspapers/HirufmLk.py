from news_lk3.core import AbstractNewsPaper


class HirufmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.hirufm.lk/',
        ]
