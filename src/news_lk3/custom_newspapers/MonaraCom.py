from news_lk3.core import AbstractNewsPaper


class MonaraCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://monara.com/',
        ]
