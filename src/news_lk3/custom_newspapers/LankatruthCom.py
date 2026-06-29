from news_lk3.core import AbstractNewsPaper


class LankatruthCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankatruth.com/home/',
        ]
