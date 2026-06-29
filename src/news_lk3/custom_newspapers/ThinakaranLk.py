from news_lk3.core import AbstractNewsPaper


class ThinakaranLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.thinakaran.lk/',
        ]
