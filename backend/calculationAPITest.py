import unittest
import json
from main import app  

class calculationAPITest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/add', data=json.dumps({'a': 10, 'b': 5}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 15)

    def test_subtraction(self):
        response = self.app.post('/subtract', data=json.dumps({'a': 10, 'b': 5}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 5)

    def test_invalid_input(self):
        response = self.app.post('/add', data=json.dumps({'a': 'invalid', 'b': 5}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
