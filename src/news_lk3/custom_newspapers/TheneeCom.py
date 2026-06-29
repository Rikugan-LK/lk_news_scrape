from news_lk3.core import AbstractNewsPaper


class TheneeCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.thenee.com/',
        ]
