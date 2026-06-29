from news_lk3.core import AbstractNewsPaper


class KottuOrg(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://kottu.org/',
        ]
