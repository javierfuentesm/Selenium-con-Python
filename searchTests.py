import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    # def test_vip_promo(self):
    # vip_promo= self.driver.find_element_by_xpath('')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1,len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
