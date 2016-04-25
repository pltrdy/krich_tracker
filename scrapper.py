#!/usr/bin/env python3
from lxml import html
import requests

debug_mode = False

def get_richlist(url, xpath, cols):	
	page = requests.get(url)
	tree = html.fromstring(page.content)	
	rows  = tree.xpath(xpath) 
	#print(listtree)
	richs = []
	for tr in rows:
		val = tr.xpath('td/text()')
		rich = {}
		debug("New row:")
		for c in cols:
			try:
				rich[c] = val[cols[c]]
			except IndexError:
				rich[c] = None
			debug("\tcol: %s\t\tval: %s" % (c, rich[c]))
		richs.append(rich)
	return richs


def debug(text):
	global debug_mode
	if debug_mode:	
		print(text)
if __name__ == '__main__':
	import sys
	import conf as c
	debug_mode = True
	print(get_richlist(c.url, c.xpath, c.columns))
