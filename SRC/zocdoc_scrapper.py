from web_scrapper import Scrapper
from html_data_extractor import HTMLDataExtractor

TOTAL_NUMBER_OF_PAGES=10

DOCTORS_LIST_OUTPUT_DIR="../HTMLS/DOCTORS_LIST/"
DOCTORS_OUTPUT_DIR="../HTMLS/DOCTORS/"=

def fetchDocList():
	manhattan_zipcodes = [10001, 10002, 10003, 10004, 10005, 10010, 10011, 10012, 10013, 10014, 10019, 10020, 10021, 10022, 10023, 10040, 10044, 10065, 10069, 10075, 10094, 10128, 10168, 10280, 10281, 10282]   
	drSpecialities=[153 #Primary Care \
		       ]
	queries = []
	for zipIdx, zipcode in enumerate(manhattan_zipcodes):
	    for offset in xrange(0,TOTAL_NUMBER_OF_PAGES):
		    for drSpeciality in drSpecialities:
	    		queries.append('dr_specialty='+str(drSpeciality)+'&address='+str(zipcode)+'&insurance_carrier=-1&refine_search=Find+a+Doctor&offset='+str(offset*10))  
	print 'Total number of queries are ', len(queries)
	print queries
        url = 'https://www.zocdoc.com/search/?'

        scrapper = Scrapper()
        return scrapper.fetchPages(url, queries, saveToFile=True, DELAY_IN_FETCH=1, fileNamePrefix='docList', outputDir=DOCTORS_LIST_OUTPUT_DIR)
	
# From all the HTML pages of doctor lists extract each doctors url and save the html page for the doctor
def saveDoctorInfoPages(doctorListHTMLs):
	urls = []
	htmlDataExtractor = HTMLDataExtractor()
	for doctorListHTML in doctorListHTMLs:
		urls = urls + htmlDataExtractor.extractDoctorsUrlsFromString(doctorListHTML)
		print urls
	base_url = 'https://www.zocdoc.com/'
	scrapper = Scrapper()
	return scrapper.fetchPages(base_url, urls, saveToFile=True, DELAY_IN_FETCH=1, fileNamePrefix='docInfo', outputDir=DOCTORS_OUTPUT_DIR)

def main():
	doctorListHTML = fetchDocList()
	saveDoctorInfoPages(doctorListHTML)




if __name__ == "__main__":
	main()
