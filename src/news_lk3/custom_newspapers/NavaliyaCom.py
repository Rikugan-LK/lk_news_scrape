from news_lk3.core import AbstractNewsPaper


class NavaliyaCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.navaliya.com/',
        ]
