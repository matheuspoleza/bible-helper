import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "bible_helper.settings"

import urllib2
import re
from bible.models import *

bible_version = 'nvi'
url = 'https://www.bibliaonline.com.br/'

for i,j in enumerate(Book.objects.values_list('cod')):
	print(j[0])
	complete_url = url+bible_version+'/'+j[0]

	response = urllib2.urlopen(complete_url)
	html = response.read()
	lista = html[html.find('ChapterList')::]

	for a in list(re.finditer(complete_url, lista)):
		string = lista[a.start()+39:a.end()+3]
		if not(string[0] == '>'):
			count = string

	print(count)