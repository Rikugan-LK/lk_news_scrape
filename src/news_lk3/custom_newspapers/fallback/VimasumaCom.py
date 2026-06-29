from news_lk3.core import AbstractNewsPaper


class VimasumaCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.vimasuma.com/',
        ]
