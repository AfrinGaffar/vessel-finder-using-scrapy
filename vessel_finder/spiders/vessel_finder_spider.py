import scrapy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from vessel_finder.items import VesselDetails
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class VesselFinderSpider(scrapy.Spider):
    name = "vessel_finder"

    def start_requests(self):
        url = "https://www.vesselfinder.com/vessels?name=9423841"
        yield scrapy.Request(url=url, callback=self.search_for_ship)

    def search_for_ship(self, response):
        search_results_link = response.css('a.ship-link::attr(href)').get()
        if search_results_link is not None:
            search_results_link = response.urljoin(search_results_link)
            yield scrapy.Request(search_results_link, callback=self.parse_ship_details)

    def parse_ship_details(self, response):
        vessel_details = VesselDetails()

        vessel_details['course_speed'] = response.css('tr:nth-child(1)').css('td:nth-child(2)::text').get()
        vessel_details['current_draught'] = response.css('tr:nth-child(2)').css('td:nth-child(2)::text').get()
        vessel_details['navigation_status'] = response.css('tr:nth-child(3)').css('td:nth-child(2)::text').get()
        vessel_details['position_received'] = response.css('tr:nth-child(4)').css('td:nth-child(2) span::text').get()
        vessel_details['imo'] = response.css('tr:nth-child(5)').css('td:nth-child(2)::text').get()
        vessel_details['call_sign'] = response.css('tr:nth-child(6)').css('td:nth-child(2)::text').get()
        vessel_details['flag'] = response.css('tr:nth-child(7)').css('td:nth-child(2)::text').get()
        vessel_details['length_beam'] = response.css('tr:nth-child(8)').css('td:nth-child(2)::text').get()

        yield vessel_details


    # def load_driver(self):
    #     """
    #     Loads Selenium Chrome webdriver. Uses headless browser to scrap.
    #     :return:
    #     """
    #     chrome_options = Options()
    #     chrome_options.add_argument("--headless")
    #     self.driver = webdriver.Chrome(chrome_options=chrome_options)
    #
    # def key_in_imo(self, imo):
    #     imo_text_box = self.driver.find_element_by_id('advsearch-name')
    #     imo_text_box.send_keys(imo)
    #
    # def click_search(self):
    #     search_button = self.driver.find_element_by_link_text('Search')
    #     search_button.click()
    #     sleep(3)
    #
    # def get_ship_link(self):
    #     ship_link = self.driver.find_element_by_class_name('ship-link')
    #     ship_link.get_attribute('href')
    #
    # def search_results_exists(self):
    #     return self.is_ele_exist(By.CLASS_NAME, 'ship-link')
    #
    # def is_ele_exist(self, by, value):
    #     return self.driver.find_elements(by, value).__len__() > 0

