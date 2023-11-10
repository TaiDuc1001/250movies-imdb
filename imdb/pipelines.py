# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class ImdbPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip all whitespace
        field_names = adapter.field_names()
        for field_name in field_names:
            value = adapter.get(field_name)
            adapter[field_name] = value.strip()

        # Year
        year = adapter.get('year')
        year = re.search(r'\d+', year)
        adapter['year'] = int(year.group()) # only take numbers and convert to integer

        # Rating
        rating = adapter.get('rating')
        adapter['rating'] = float(rating) # convert to float

        # Rank
        rank = adapter.get('rank')
        adapter['rank'] = rank.replace('.', '')



        return item
