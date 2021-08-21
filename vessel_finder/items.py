# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class VesselDetails(scrapy.Item):
    course_speed = Field()
    current_draught = Field()
    navigation_status = Field()
    position_received = Field()
    imo = Field()
    call_sign = Field()
    flag = Field()
    length_beam = Field()
