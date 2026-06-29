from news_lk3.core import AbstractNewsPaper


class BbcCoUkTamil(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.bbc.co.uk/tamil/',
        ]
