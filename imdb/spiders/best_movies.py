from typing import Iterable
import scrapy
from scrapy.http import Request
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from imdb.items import MoviesItem


class BestMoviesSpider(scrapy.Spider):
    name = "best_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating"]
    
    def parse(self, response):
        movies = response.css('.lister-list .lister-item.mode-advanced')

        movies_item = MoviesItem()
        for movie in movies:
            movies_item['rank'] = movie.css('.lister-item-index::text').get()
            movies_item['title'] = movie.css('h3 a::text').get()
            movies_item['year'] = movie.css('.lister-item-year::text').get()
            movies_item['duration'] = movie.css('.runtime::text').get()
            movies_item['genre'] = movie.css('.genre::text').get()
            movies_item['rating'] = movie.css('.ratings-imdb-rating strong::text').get()
            movies_item['vote'] = movie.xpath('.//p[@class="sort-num_votes-visible"]/span[2]/text()').get()
            movies_item['gross'] = movie.xpath('.//p[@class="sort-num_votes-visible"]/span[5]/text()').get()
            movies_item['description'] = movie.xpath('.//div[@class="lister-item-content"]/p[2]/text()').get()

            yield movies_item

        desc = response.css('.desc a')
        if len(desc) > 2:
            relative_url = response.xpath('//*[@id="main"]/div/div[1]/div[2]/a[2]/@href').get()
        else:
            relative_url = response.xpath('//*[@id="main"]/div/div[1]/div[2]/a/@href').get()

        absolute_url = 'https://imdb.com' + relative_url
        yield response.follow(absolute_url, callback=self.parse)
