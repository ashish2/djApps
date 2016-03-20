#!/usr/bin/python
from django.shortcuts import render

# Create your cli scripts here.

class Billing:
	
	@staticmethod
	def getNextBillingDueDate(typ, cd, tt=None):
		import datetime as d
		import dateutil as dt
		da = d.datetime.strptime(cd, "%Y-%m-%d")
		#tt = d.date.today()
		if not tt:
			tt = d.datetime.today()
		else:
			tt = d.datetime.strptime(tt, "%Y-%m-%d")
		
		if typ == "postpaid":
			curr_date = d.datetime( tt.year, tt.month, 24)
			if tt.day >= 24:
				# next_month # adding month
				next_month_24 = curr_date + dt.relativedelta.relativedelta(months=1)
				return next_month_24
			else:
				# current_month_24 # this month
				current_month_24 = curr_date
				return current_month_24
		elif typ == "prepaid":
			# add a year from today, month & day from created_at
			# next_year_24_jan = d.datetime( tt.year, da.month, 24) + dt.relativedelta.relativedelta(years=1)
			next_year_24_jan = d.datetime( tt.year, da.month, da.day) + dt.relativedelta.relativedelta(years=1)
			return next_year_24_jan
		else:
			return False


#getNextBillingDueDate(typ, cd, tt)


