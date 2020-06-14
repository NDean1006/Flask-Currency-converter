from unittest import TestCase
from app import app
from convert import Convert


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True
       
    def test_homepage(self):
        """Make sure INDEX HTML is displayed"""

        with self.client:
            response = self.client.get('/')
            self.assertIn(b'<lable for="form">Converting From</lable>\n', response.data)
            self.assertIn(b'<lable for="to">Converting To</lable>\n', response.data)
            self.assertIn(b'<lable for="amount">Amount</lable>\n', response.data)

    def test_convert(self):
        """Make sure Convert HTML is displayed"""

        with self.client:
            response = self.client.get('/convert?from=USD&to=USD&amount=1')
            self.assertIn(b'<h3>The result is', response.data)
    
    def test_exchange(self):
        """ """
        c = Convert()
        self.assertEqual(c.exchange("USD","USD", "1"), "1.00")

    def test_all_true(self):
        """ """
        c = Convert()
        self.assertTrue(c.all_true("USD", "USD", 1))
        self.assertTrue(c.all_true("USD", "GBP", 1))
        self.assertTrue(c.all_true("USD", "USD", 1))

    def test_get_currency_code(self):
        """  """
        c = Convert()
        self.assertEqual(c.get_currency_code('GBP'),"£")
        self.assertNotEqual(c.get_currency_code('USD'),"£")

    def test_check_valid_currency(self):
        """  """
        c = Convert()
        self.assertTrue(c.check_valid_currency('HKD'))
        self.assertTrue(c.check_valid_currency('USD'))

    def test_check_amount_data_type(self):
        """  """
        c = Convert()
        self.assertTrue(c.check_amount_data_type(3215654))
        self.assertTrue(c.check_amount_data_type(3215654))

    def test_check_valid_amount(self):
        """  """
        c = Convert()
        self.assertTrue(c.check_valid_amount(120))
        self.assertTrue(c.check_valid_amount(1))
        self.assertTrue(c.check_valid_amount(1.1))

    




    
