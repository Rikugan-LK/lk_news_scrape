from news_lk3.core import AbstractNewsPaper


class NeruppuCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://neruppu.com/',
        ]
