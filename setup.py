from setuptools import setup, find_packages

setup(
    name='goodreads_scraper',
    version='1.0',
    packages=find_packages(),
    package_data={
        'goodreads_scraper': ['data/*.csv'],
    },
    entry_points={
        'scrapy': ['settings = goodreads_scraper.settings']
    },
    install_requires=[
        'scrapy>=2.11.0',
        'scrapy-user-agents>=0.1.1'
    ],
    zip_safe=False
)
