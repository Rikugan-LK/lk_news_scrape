from news_lk3.core import AbstractNewsPaper


class LankabusinessonlineCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.lankabusinessonline.com/',
        ]
