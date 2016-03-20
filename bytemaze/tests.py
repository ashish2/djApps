from django.test import TestCase
import unittest

# Create your tests here.
from cliscripts import Billing
import datetime as d


class BillingTestCase(unittest.TestCase):
	
	def test_getNextBillingDueDate(self):
		typ, cd, tt = "postpaid", "2016-01-01", "2016-03-23"
		ret = Billing.getNextBillingDueDate(typ, cd, tt)
		self.assertEqual(ret, d.datetime(2016, 03, 24))
		
		typ, cd, tt = "postpaid", "2016-01-01", "2016-03-24"
		ret = Billing.getNextBillingDueDate(typ, cd, tt)
		self.assertEqual(ret, d.datetime(2016, 04, 24))
		
		typ, cd, tt = "prepaid", "2016-02-01", "2016-04-23"
		ret = Billing.getNextBillingDueDate(typ, cd, tt)
		self.assertEqual(ret, d.datetime(2017, 02, 01))
		
		typ, cd, tt = "prepaid", "2016-01-31", "2017-04-23"
		ret = Billing.getNextBillingDueDate(typ, cd, tt)
		self.assertEqual(ret, d.datetime(2018, 01, 31))
		

