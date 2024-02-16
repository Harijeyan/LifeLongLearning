import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Article

class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Pathum_Nissanka"]

    # Set a custom user-agent and download delay to be polite
    custom_settings = {
        'user_agent': 'hobby_crawler (email@example.com)',
        'download_delay': 2,  # 2 seconds of s
        'FEED_URI' : 'articles.xml',
        'FEED_FORMAT' : 'xml'
    }

    # Adjust the rules to follow only allowed URLs, excluding those disallowed by robots.txt
    rules = [
        Rule(
            LinkExtractor(
                allow=(
                    '/wiki/[^:]+$'  # Matches all 'wiki/' paths that do not contain a colon
                ),
                deny=(
                    '/wiki/Special:', '/wiki/Talk:', '/wiki/Portal:', 
                    '/wiki/File:', '/wiki/Category:', '/wiki/Help:', '/wiki/Template:'
                    # Add any other namespaces or paths you find in robots.txt that should be excluded
                )
            ),
            callback='parse_info',
            follow=True
        )
    ]

    def parse_info(self, response):
        article = Article()
        article['title'] = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()')
        article['url'] = response.url
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()')
        return article