from news_lk3.core import AbstractNewsPaper


class LankapuvathLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankapuvath.lk/',
        ]
