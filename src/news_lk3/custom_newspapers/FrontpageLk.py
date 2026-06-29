from news_lk3.core import AbstractNewsPaper


class FrontpageLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.frontpage.lk/',
        ]
