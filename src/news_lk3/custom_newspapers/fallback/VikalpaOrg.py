from news_lk3.core import AbstractNewsPaper


class VikalpaOrg(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.vikalpa.org/',
        ]
