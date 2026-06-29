from news_lk3.core import AbstractNewsPaper


class LankacnewsCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://lankacnews.com/english/',
        ]
