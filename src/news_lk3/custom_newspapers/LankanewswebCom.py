from news_lk3.core import AbstractNewsPaper


class LankanewswebCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankanewsweb.com/',
        ]
