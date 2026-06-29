from news_lk3.core import AbstractNewsPaper


class Col3negoriginalCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.col3negoriginal.com/',
        ]
