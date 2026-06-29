from news_lk3.core import AbstractNewsPaper


class BudusaranaLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://www.budusarana.lk/',
        ]
