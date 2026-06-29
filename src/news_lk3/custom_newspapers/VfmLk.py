from news_lk3.core import AbstractNewsPaper


class VfmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://www.vfm.lk/',
        ]
