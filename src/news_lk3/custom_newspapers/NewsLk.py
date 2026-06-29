from news_lk3.core import AbstractNewsPaper


class NewsLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.news.lk/',
        ]
