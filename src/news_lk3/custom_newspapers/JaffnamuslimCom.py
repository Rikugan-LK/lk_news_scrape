from news_lk3.core import AbstractNewsPaper


class JaffnamuslimCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.jaffnamuslim.com/',
        ]
