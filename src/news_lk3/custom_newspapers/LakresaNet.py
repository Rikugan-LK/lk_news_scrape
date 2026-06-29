from news_lk3.core import AbstractNewsPaper


class LakresaNet(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lakresa.net/',
        ]
