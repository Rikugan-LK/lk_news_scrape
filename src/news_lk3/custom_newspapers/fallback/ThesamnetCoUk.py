from news_lk3.core import AbstractNewsPaper


class ThesamnetCoUk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://thesamnet.co.uk/',
        ]
