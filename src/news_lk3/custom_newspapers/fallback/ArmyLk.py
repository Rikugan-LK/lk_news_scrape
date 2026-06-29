from news_lk3.core import AbstractNewsPaper


class ArmyLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.army.lk/',
        ]
