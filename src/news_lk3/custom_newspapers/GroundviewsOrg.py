from news_lk3.core import AbstractNewsPaper


class GroundviewsOrg(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.groundviews.org/',
        ]
