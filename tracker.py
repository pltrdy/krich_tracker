#!/usr/bin/python3

import json 
import os
import scrapper
from datetime import datetime
import time

mandatory = ['refresh', 'path', 'url', 'xpath', 'columns']

class Tracker:
	def __init__(self,  conf):
		self.conf = self.check_conf(conf)
		self.data = self.load()
	
	def check_conf(self, path):
		c = __import__(path)

		for m in mandatory:
			if not hasattr(c, m):
				raise Exception("Parameter '%s' missing from configuration file" % m)
		return c

	def load(self):
		if os.path.exists(self.conf.path):
			with open(self.conf.path, 'r') as data_file:
				data = json.load(data_file)
				
		else:
			data = {}
		return data

	def save(self):
		with open(self.conf.path, 'w+') as file:
			json.dump(self.data, file)

	def run(self):
		while True:
			now = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
			print("[%s] Updating..." % now)
			richlist = scrapper.get_richlist(self.conf.url, self.conf.xpath, self.conf.columns)

			for r in richlist:
				record = {"time": now}
				for v in r:
					record[v] = r[v]
				
				if r['address'] in self.data:
					self.data[r['address']]['records'].append(record)

				else:
					self.data[r['address']] = { "records": [record]}


			self.save()
			refresh = int(self.conf.refresh)
			print("Sleeping for %dsec" % refresh)
			time.sleep(refresh)			


if __name__ == '__main__':	
	import sys
	if len(sys.argv) == 2:	
		t = Tracker(sys.argv[1])
		t.run()
	else:
		print("Missing parameter: configuration module")
