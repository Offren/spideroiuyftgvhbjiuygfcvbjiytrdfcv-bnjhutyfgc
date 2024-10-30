BOT_NAME = 'goodreads_scraper'

SPIDER_MODULES = ['goodreads_scraper.spiders']
NEWSPIDER_MODULE = 'goodreads_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performing at the same time to the same domain
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 3

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'goodreads_scraper.pipelines.GoodreadsScraperPipeline': 300,
}

# Enable and configure HTTP caching
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Custom settings
FEEDS = {
    'profiles.csv': {
        'format': 'csv',
        'fields': ['url', 'source_url'],
        'overwrite': True
    }
}