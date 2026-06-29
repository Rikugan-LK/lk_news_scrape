from news_lk3.core import AbstractNewsPaper


class OnlineuthayanCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://onlineuthayan.com/',
        ]
