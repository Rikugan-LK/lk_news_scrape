from news_lk3.core import AbstractNewsPaper


class EuthayanCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.euthayan.com/',
        ]
