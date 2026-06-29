from news_lk3.core import AbstractNewsPaper


class RhythmfmLk(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'https://rhythmfm.lk/',
        ]
