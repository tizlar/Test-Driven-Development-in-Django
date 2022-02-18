from django.test import TestCase
from selenium import webdriver

# class FunctionalTestCase(TestCase):

    # def setUp(self):
    #     self.browser = webdriver.Firefox()
    #
    # def test_there_is_homepage(self):
    #     self.browser.get('http://localhost:8000')
    #     self.assertIn('Enter hash here:', self.browser.page_source)
    #
    # def test_hash_of_hello(self):
    #     self.browser.get('http://localhost:8000')
    #     text = self.browser.find_element_by_id('id_text')
    #     text.send_keys('hello')
    #     self.browser.find_element_by_name('submit').click()
    #     self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.browser.page_source)
    #
    # def tearDown(self):
    #     self.browser.quit()

class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing\home.html')
