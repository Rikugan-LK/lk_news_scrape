from news_lk3.core import AbstractNewsPaper


class RedfmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://redfm.lk/',
        ]
