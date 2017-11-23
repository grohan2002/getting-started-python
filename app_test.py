from app import app

import unittest
import json

class CitiesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response-city = tester.get('/cities.json', content_type='application/json')
    self.assertEqual(response-city.status_code, 200)
    self.assertEqual(response-city.data, json.dumps({"cities" : ["Amsterdam", "Berlin", "New York", "San Francisco", "Tokyo", "Mumbai"]}))
    response-countries = tester.get('/countries.json', content_type='application/json')
    self.assertEqual(response-countries.status_code, 200)
    self.assertEqual(response-countries.data, json.dumps({"cities" : ["Netherlands", "Germany", "US-East", "US-West", "Tokyo", "India"]}))

if __name__ == '__main__':
    unittest.main()
