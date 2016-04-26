"""
	Tracker configuration
"""

# Time between each iteration, seconds
refresh = 60*5

# Path to datafile
path = "data.json"

"""
	 Scrapper configuration
"""
# Richlists URL 
url = "http://gaiaplatform.com/kr/richlist.php"

# XPATH Query - see. http://www.w3schools.com/xsl/xpath_syntax.asp
xpath = "//div[@role='main']/table/tbody/tr"

# Dictionnary of columns. keys are name of the columns, values are 
# the positions (left to right)
columns = {"rank":0, "address":1, "balance":2, "last_tansaction":3, "label": 4}
