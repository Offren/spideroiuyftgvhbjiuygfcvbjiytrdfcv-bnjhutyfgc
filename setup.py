from setuptools import setup, find_packages

setup(
    name='goodreads_scraper',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'goodreads_scraper': ['data/*.csv'],
    },
    install_requires=[
        'scrapy>=2.11.0',
        'scrapy-user-agents>=0.1.1'
    ]
)
