import sys
import os
sys.path.append('src')

from news_lk3.custom_newspapers.NewswireLk import NewswireLk
from lk_news.NewsArticle import NewsArticle

print("Newspaper ID:", NewswireLk.get_newspaper_id())
try:
    urls = list(NewswireLk.gen_article_urls())
    print("Found article URLs count:", len(urls))
    if urls:
        print("First URL:", urls[0])
        article = NewswireLk.parse_article(urls[0])
        print("Article Title:", getattr(article, "original_title", "N/A"))
        print("Article Body Lines:", len(getattr(article, "original_body_lines", [])))
        print("Article Publish Time:", getattr(article, "time_ut", "N/A"))
except Exception as e:
    import traceback
    traceback.print_exc()
