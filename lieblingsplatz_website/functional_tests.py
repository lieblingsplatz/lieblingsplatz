from selenium import webdriver
from selenium.webdriver.common.by import By
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
        #file_name = "../scrape/150823_kitas_test.csv"
        file_name = "../scrape/160123_kitas_arbeitsstand_helen_500.csv"
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

        #check for the existence of the leaflet.js libraries
        js_files = self.browser.find_elements(By.TAG_NAME, "script")
        js_file_locations = [file.get_attribute("src") for file in js_files]
        expected_js_location = 'http://cdn.leafletjs.com/leaflet-0.7.5/leaflet.js'
        self.assertIn(expected_js_location, js_file_locations)

        css_files = self.browser.find_elements(By.TAG_NAME, "link")
        css_file_locations = [file.get_attribute("href") for file in css_files]
        expected_css_location = 'http://cdn.leafletjs.com/leaflet-0.7.5/leaflet.css'
        self.assertIn(expected_css_location, css_file_locations)

        #check for the existence and proper size of the map
        map = self.browser.find_element_by_id("map")
        expected_size = "786px"
        self.assertEqual(expected_size, map.value_of_css_property("height"))

        self.fail("Finish test!")

if __name__ == '__main__':
    unittest.main()