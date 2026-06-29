from news_lk3.core import AbstractNewsPaper


class LankanewspapersCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankanewspapers.com/',
        ]
