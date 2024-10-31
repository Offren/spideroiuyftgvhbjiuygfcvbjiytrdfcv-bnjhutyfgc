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

# Enable and configure AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Zyte-specific settings
EXTENSIONS = {
    'scrapy.extensions.throttle.AutoThrottle': None,
    'sh_scrapy.extension.HubstorageExtension': 500,
}

# Memory management
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 950
MEMUSAGE_WARNING_MB = 850

# Retry configuration
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# Cache settings
HTTPCACHE_ENABLED = False  # Disable cache on Zyte

# Log settings
LOG_LEVEL = 'INFO'
LOG_ENABLED = True
