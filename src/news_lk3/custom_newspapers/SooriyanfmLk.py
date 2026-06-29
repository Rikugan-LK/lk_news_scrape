from news_lk3.core import AbstractNewsPaper


class SooriyanfmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.sooriyanfm.lk/',
        ]
