from metapub import PubMedFetcher
#from metapub import FindIt
#from Bio import Entrez
import scholarly
import numpy as np
#import json
#import objectpath
import webbrowser
import html2text
from ast import literal_eval
import urllib.request
from bs4 import BeautifulSoup
import re

#stage I
#to run the first section type the command as python cp.py > trial.txt	   
fetch = PubMedFetcher()
counter=0
# get the first 1000 pmids matching "breast neoplasm" keyword search
pmids = fetch.pmids_for_query('fragile sites', retmax=2)
print (pmids)

retmax=20
#in order to store data in a relevant format 
print ('[')
for pmid in pmids:
	counter+=1
	#print (pmid)
	article = fetch.article_by_pmid(pmid)
	title=article.title
	#print (title)
	
	search_query=scholarly.search_pubs_query(title)
	print(next(search_query))
	#print (res)
	if (counter!=retmax):
		print (',')

print (']')



#stage II

def extract(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

def convert(s): 
    string = "" 
    return(string.join(s)) 
      

with open('trial.txt') as f:
    prev_cnt=0
    current_cnt=0
    dictionaries = literal_eval(f.read().strip()) 
    #print (dictionaries)
    for d in dictionaries:
      current_cnt+=1
      u=d['bib']['url']
      #webbrowser.open(u)
      html = urllib.request.urlopen(u)
      soup = BeautifulSoup(html)
      #print (soup.get_text)
      data = soup.findAll(text=True)
      result = filter(extract, data)
      
      #print (list(result))
      content=list(result)
      


      print (content)
      #print (info)
      #stage III
      if (prev_cnt != current_cnt):
      	file=open('file%d.html' % current_cnt,'w+')
      	for listitem in content:
        	file.write('%s\n' % listitem)

      	file.close()
  


	
	
