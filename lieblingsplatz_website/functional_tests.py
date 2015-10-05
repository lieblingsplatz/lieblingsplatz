from selenium import webdriver
import unittest
from kita_importer import importer


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        #self.insert_test_data_into_db()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def insert_test_data_into_db(self):
        file_name = "../scrape/150823_kitas_test.csv"
        importer.import_csv_into_db(file_name)


    def test_can_see_kitas_in_english(self):
        self.browser.get('http://localhost:8000/list-kitas')
        self.assertIn('Lieblingsplatz', self.browser.title)

        headers = self.browser.find_elements_by_class_name("header")
        header_texts = [header.text for header in headers]
        self.assertIn("Name:", header_texts)
        self.assertIn("Senats_Id:", header_texts)
        self.assertIn("Address:", header_texts)
        self.assertIn("Zip_Code:", header_texts)
        self.assertIn("District:", header_texts)
        self.assertIn("Latitude:", header_texts)
        self.assertIn("Longitude:", header_texts)


    def test_can_see_map_with_kitas_in_english(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('Lieblingsplatz', self.browser.title)

        #check for existence of the map
        map = self.browser.find_element_by_id("map")

        self.fail("Finish test!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')