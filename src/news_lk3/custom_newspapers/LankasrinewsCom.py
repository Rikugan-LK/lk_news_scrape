from news_lk3.core import AbstractNewsPaper


class LankasrinewsCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankasrinews.com/',
        ]
