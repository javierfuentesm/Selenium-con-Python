import csv
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


def get_data(filename):
    rows = []
    data_file = open(filename, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(*get_data('testData.csv'))
    @unpack
    def test_search_dtt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        # print(f'Found {len(products)} productos')
        #
        # for product in products:
        #     print(product.text)
        #
        # self.assertEqual(expected_count, len(products))

        expected_count = int(expected_count)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)

        print(f'Found {len(products)} productos')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
