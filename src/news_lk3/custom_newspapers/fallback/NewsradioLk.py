from news_lk3.core import AbstractNewsPaper


class NewsradioLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://newsradio.lk/',
        ]
