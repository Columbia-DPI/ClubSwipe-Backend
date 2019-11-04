import unittest
 
from app import app 

class AutomationTests(unittest.TestCase):


    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass

    # BEGINREGION - Unit Tests

    # Begin test to check main React page response
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ENDREGION - Unit Tests

if __name__ == "__main__":
    unittest.main()
