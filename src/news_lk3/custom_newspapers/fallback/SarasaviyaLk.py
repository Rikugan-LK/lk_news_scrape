from news_lk3.core import AbstractNewsPaper


class SarasaviyaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.sarasaviya.lk/',
        ]
