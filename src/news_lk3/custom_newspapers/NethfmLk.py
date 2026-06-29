from news_lk3.core import AbstractNewsPaper


class NethfmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://nethfm.lk/',
        ]
