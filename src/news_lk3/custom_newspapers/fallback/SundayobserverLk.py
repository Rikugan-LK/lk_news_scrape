from news_lk3.core import AbstractNewsPaper


class SundayobserverLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.sundayobserver.lk/',
        ]
