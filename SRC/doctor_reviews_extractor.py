from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

DOCTORS_DIR='/Users/Santosh/PROJECTS/ZOCDOC_ML/HTMLS/DOCTORS/'
OUTPUT_CSV_NAME='../DATA/zocdocData2.csv'
cma=','

def repc(string):
	return string.replace(cma, ' ').replace('\r\n', ' ')

class DoctorReviewsExtractor:
	def __init__(self):
		pass

	def extractReviewsToCSV(self, outputCSVFileName=OUTPUT_CSV_NAME, inputDir=DOCTORS_DIR):
		 docFiles = [ join(DOCTORS_DIR,f)  for f in listdir(DOCTORS_DIR) if isfile(join(DOCTORS_DIR, f)) ]
		 zocdoc_csv_file = open(outputCSVFileName, "w")
		 print 'DocName,DocDegree,Location,PatientName,ReviewDate,OverallRating,BedsideMannerRating,WaitTimeRating,Review'
		 for f in docFiles:
		     with open (f, "r") as docFile:
			docHtml=docFile.read()
			soup = BeautifulSoup(docHtml)
			try:
				docInfo = soup.head.title.string.split("-")
				docDegreeLoc = docInfo[1]
				docDegree = docDegreeLoc.split('(')[0].strip(' ')
				docLoc = docDegreeLoc.split('(')[1].strip(' ')[:-1]
				docName = docInfo[0]
				for div in soup.findAll('div', 'reviewsMain'):
					try:
						reviewdt=""
						reviewerName=""
						for child in div.div.descendants:
							if child.name == 'span':
								if child['itemprop'] == 'author':
									reviewerName = child.string[3:]
								if child['itemprop'] == 'datePublished':
									reviewdt = child.string
						for sibling in div.div.next_siblings:
							if sibling.name == 'div':
								if sibling['class'][0] == 'reviewCell' and sibling['class'][1] == 'rec':
									overallRating = self.__getRatingFromText(sibling.div.div['class'][1])
								if sibling['class'][0] == 'clearfix':
									bedsideRating = self.__getRatingFromText(sibling.div.div.div['class'][1])
									for wt in sibling.findAll('div','reviewCell'):
										if wt['class'][1] == 'waittime':
											waitTimeRating = self.__getRatingFromText(wt.div.div['class'][1])
								if sibling['class'][0] == 'reviewCell' and sibling['class'][1] == 'comments':
									review=sibling.p.string
						print (repc(docName)+ cma+ repc(docDegree)+ cma+ repc(docLoc) + cma + repc(reviewerName)+ cma+ repc(reviewdt)+ cma+ str(overallRating)+ cma+ str(bedsideRating)+ cma+ str(waitTimeRating)+ cma+ repc(review))

					except:
						pass
									
			except:
		 		pass
			zocdoc_csv_file.close()
	def __getRatingFromText(self, text):
		if text == 'sg-rating-5_0':
			return 5
		if text == 'sg-rating-4_0':
			return 4
		if text == 'sg-rating-3_0':
			return 3
		if text == 'sg-rating-2_0':
			return 2
		if text == 'sg-rating-1_0':
			return 1
		return 0
def main():
	doctorReviewsExtractor = DoctorReviewsExtractor()
	doctorReviewsExtractor.extractReviewsToCSV()

if __name__ == "__main__":
	main()
