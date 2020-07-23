import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_fields = driver.find_element_by_name('q')
        search_fields.clear()
        search_fields.send_keys('tee')
        search_fields.submit()
        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()
        alert = driver.switch_to.alert()
        alert_text = alert.text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
