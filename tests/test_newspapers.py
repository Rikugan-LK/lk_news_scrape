import unittest

from news_lk3 import AdaDeranaLk


class TestCase(unittest.TestCase):

    def test_single(self):
        newspaper_cls = AdaDeranaLk
        article_list = list(newspaper_cls.gen_articles(set()))
        self.assertGreater(len(article_list), 0)
