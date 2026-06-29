from news_lk3.core import AbstractNewsPaper


class SrilankamirrorCom(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            'http://www.srilankamirror.com/',
        ]
