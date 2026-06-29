from news_lk3.core import AbstractNewsPaper


class NewswireLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://www.newswire.lk/',
        ]
