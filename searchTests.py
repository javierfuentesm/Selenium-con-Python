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
       self.assertEqual(3,len(banners))

    def




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes',report_name='hello-world-report'))
