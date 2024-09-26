import unittest
from nacha_app.account import Account

class TestAccount(unittest.TestCase):

    def test_receive_payment(self):
        acc = Account('12345', acc_bal=50.00)
        self.assertEqual(acc.receive_payment)
