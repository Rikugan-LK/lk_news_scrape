from news_lk3.core import AbstractNewsPaper


class VivalankaCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.vivalanka.com/',
        ]
