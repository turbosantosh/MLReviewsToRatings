# Web Scraping Component API
## Fetch data from Zocdoc websites for all Primary Care Physicians in Manhattan

import time
import requests

WHITESPACES=' '
WHITESPACE_SUBSTITUTE='\%20'
HTML_EXT='.html'
CURRENT_DIR="./"

# Responsible for fetching url pages with queries
class Scrapper():
	def __init__(self):
		return

	# url is the base url including '?'. Example: 'https://www.zocdoc.com/search/?'
	# queries is the list of queries that we want to run to fetch the pages
		# If queries is empty simply try fetchin the given URL
		# Example: ['dr_specialty=153&address=10001&insurance_carrier=-1&refine_search=Find+a+Doctor&offset=10']
	# saveToFile is False then returns a list of html content
	# if True, then fileNamePrefix is needed. Files are saved as html files with fileNamePrefix+indexInQueries+".html"
	# DELAY_IN_FETCH is the delay in seconds with which every page is fetched. Please insert some delays
	def fetchPages(self, url, queries=[], fileNamePrefix='tmpOutput01231123', saveToFile=False, DELAY_IN_FETCH=2, outputDir=CURRENT_DIR):
		htmlPages=[]
		if not queries:
		# Assumption is if no queries are present then simply fetch the url	
			html = self.__fetchUrl(url, DELAY_IN_FETCH)
			if saveToFile:
				self.__saveAsHTML(html, fileNamePrefix, outputDir)
			htmlPages.append(html)
			return htmlPages

		outFileIdx=0
		for queryIdx, query in enumerate(queries):
		    # Subsitiute escape sequences
		    url = url + query.replace(WHITESPACES, WHITESPACE_SUBSTITUTE)
	            html=self.__fetchUrl(url, DELAY_IN_FETCH)
		    if saveToFile:
			self.__saveAsHTML(html, fileNamePrefix+str(outFileIdx), outputDir)
		    htmlPages.append(html)
		    outFileIdx = outFileIdx + 1
		return htmlPages

	def __fetchUrl(self, url, DELAY_IN_FETCH=2):
		req = requests.get(url)
		time.sleep(DELAY_IN_FETCH)
		return req.text.encode('utf-8')

	def __saveAsHTML(self, html, fileName, outputDir=CURRENT_DIR):
		text_file = open(outputDir+"/"+fileName+HTML_EXT, "w")
		text_file.write(html)
		text_file.close()      


# Test Driver
def main():
	url = 'https://www.zocdoc.com/search/?'
	queries = ['dr_specialty=153&address=10001&insurance_carrier=-1&refine_search=Find+a+Doctor&offset=10']
	scrapper = Scrapper()
	print url + queries[0]
	scrapper.fetchPages(url, queries, saveToFile=True, fileNamePrefix='docList', outputDir="../DATA/")


if __name__ == "__main__":
	main()
