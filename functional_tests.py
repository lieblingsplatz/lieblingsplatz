from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_kitas(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Lieblingsplatz', self.browser.title)
        self.fail('Test more stuff')

if __name__ == '__main__':
    unittest.main(warnings='ignore')