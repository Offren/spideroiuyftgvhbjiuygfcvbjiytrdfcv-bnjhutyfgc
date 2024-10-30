from setuptools import setup, find_packages

setup(
    name='goodreads_scraper',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = goodreads_scraper.settings']},
    install_requires=[
        'scrapy',
        'scrapy-user-agents'
    ]
)