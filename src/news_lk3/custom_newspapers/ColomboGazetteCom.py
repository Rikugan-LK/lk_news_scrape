from news_lk3.core import AbstractNewsPaper


class ColomboGazetteCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://colombogazette.com/',
        ]
