from news_lk3.core import AbstractNewsPaper


class SathhandaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://sathhanda.lk/',
        ]
