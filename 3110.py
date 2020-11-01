import requests
import unittest
SUCSESS_CODE=200
sites_list=['https://tut.by', 'https://onliner.by', 'https://rabota.by', 'https://ebay.com', 'https://kufar.by']
class TestSites(unittest.TestCase):
	def test_sites_list(self):
		for site in sites_list:
			r=requests.get(site)
			self.assertEqual(r.status_code, SUCSESS_CODE)
			print(site)