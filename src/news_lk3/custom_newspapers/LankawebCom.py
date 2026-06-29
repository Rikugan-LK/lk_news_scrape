from news_lk3.core import AbstractNewsPaper


class LankawebCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankaweb.com/',
        ]
