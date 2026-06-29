from news_lk3.core import AbstractNewsPaper


class EnglishLankaviewsCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://english.lankaviews.com/',
        ]
