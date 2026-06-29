from news_lk3.core import AbstractNewsPaper


class SunfmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.sunfm.lk/',
        ]
