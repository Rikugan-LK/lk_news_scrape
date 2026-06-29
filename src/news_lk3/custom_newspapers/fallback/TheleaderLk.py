from news_lk3.core import AbstractNewsPaper


class TheleaderLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://theleader.lk/',
        ]
