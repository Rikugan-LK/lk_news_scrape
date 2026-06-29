from news_lk3.core import AbstractNewsPaper


class FmderanaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.fmderana.lk/',
        ]
