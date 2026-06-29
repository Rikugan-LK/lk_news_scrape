from news_lk3.core import AbstractNewsPaper


class YesfmonlineCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.yesfmonline.com/',
        ]
