from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

class HTMLDataExtractor:
	def __init__(self):
		pass

	def extractDoctorsUrlsFromString(self, doctorsListHTML):
	    urls = []
	    soup = BeautifulSoup(doctorsListHTML)
	    all_divs = soup.body.find_all_next('div')
	    
	    for div in all_divs:
		try:
		    if div['class'][0] == 'profilePhoto':
		    	urls.append(div.a['href'])
		except:
		    pass
	    return urls
		
	def extractDoctorsInfoFromFile(self, htmlFullFileName):
		with open(htmlFullFIleName, 'r') as doctorsInfoHTMLFile:
			doctorsListHTML = doctorsInfoHTMLFile.read()
			return extractDoctorsUrlsFromString(doctorsListHTML)
	
