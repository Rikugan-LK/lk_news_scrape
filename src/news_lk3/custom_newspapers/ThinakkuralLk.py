from news_lk3.core import AbstractNewsPaper


class ThinakkuralLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.thinakkural.lk/',
        ]
