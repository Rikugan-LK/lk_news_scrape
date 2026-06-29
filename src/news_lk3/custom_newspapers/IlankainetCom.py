from news_lk3.core import AbstractNewsPaper


class IlankainetCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.ilankainet.com/',
        ]
