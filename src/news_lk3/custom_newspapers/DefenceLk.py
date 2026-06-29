from news_lk3.core import AbstractNewsPaper


class DefenceLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.defence.lk/',
        ]
