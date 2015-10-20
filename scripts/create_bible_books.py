import os, sys, json, requests, unicodedata, string
rest = 'http://localhost:8000/books.json'
bible_book_data = './bible_books.json'

print('1# - Setting django module into script')
# Setup script to get Django data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "bible_helper.settings"

# Communs functions
def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters).lower()

def getJsonValues(data):
	print('#2 - Getting values from json data')

	testament = 'old'
	if(data[2] == 'Mateus'):
		testament = 'new'
	return {'cod': remove_accents(data[1]), 'name': data[2], 'short_name': data[3], 'testament': testament}	

def main():
	print('#3 - Setting data to http request')
	with open(bible_book_data) as bible_books:    
	    bible_books = json.load(bible_books)

	for index,data in enumerate(bible_books):
		try:
			requests.post(rest, data=getJsonValues(data))
			print '#4 - SUCCESS - Method: POST to'+ rest
		except ValueError:
			print '#4- ERROR - Cannot request to ' + rest

main()