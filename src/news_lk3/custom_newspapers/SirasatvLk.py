from news_lk3.core import AbstractNewsPaper


class SirasatvLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://sirasatv.lk/',
        ]
