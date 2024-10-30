BOT_NAME = 'goodreads_scraper'

SPIDER_MODULES = ['goodreads_scraper.spiders']
NEWSPIDER_MODULE = 'goodreads_scraper.spiders'

# Don't obey robots.txt since we're respecting rate limits
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performing at the same time to the same domain
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Configure a delay for requests for the same website (3 seconds)
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

# Add retry middleware settings
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# Add custom settings
COOKIES_ENABLED = True
DOWNLOAD_TIMEOUT = 180
REDIRECT_ENABLED = True

# Add request headers
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}
