from bs4 import BeautifulSoup
import dbconnection
import hashcache
import re
import requests
import os
import time

#Own packages
import hashlib
import alert






def hash_file(url,site):
	'''
	Download file and hash
	'''
	hash_name = hashlib.md5(url)
	print(hash_name.hexdigest())

	r = requests.get(url)
	with open('/files/'+hash_name.hexdigest(), 'wb') as f:  
		f.write(r.content)
	hasher = hashlib.md5()
	with open('/files/'+hash_name.hexdigest(), 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
	alert.print_message("File="+url+" Hash="+hasher.hexdigest())
	

	#We have a file lets see if we have a hashed version
	

	db_file_hash=False
	#Do we have a cache  for this file
	db_file_hash = hashcache.check_hash_redis(hash_name.hexdigest())
	if db_file_hash == False:
		#We dont have a cached version check in the db else add it there
		db_file_hash = dbconnection.add_file_db(url,hash_name.hexdigest(),hasher.hexdigest(),r.content,site)
		if db_file_hash != False:
			# We got back a has from the db lets check it 
			check_the_hash(db_file_hash,hasher.hexdigest())
		else:
			#Was a new file so lets pass now
			alert.print_message("Adding the file into the db")
	else:
		alert.print_message("Yess we hade the values in cache !!")
		check_the_hash(db_file_hash,hasher.hexdigest())




def check_the_hash(site_hash, db_hash):
	'''
	Here is where we check the hash to se if they are the same
	'''


	if site_hash == db_hash:
		# We have the same hash on the site as in our db
		# So we are good :-)
		alert.print_message("All fine the hash matched") 
	else:
		# Well now we have a problem the hash in the db and from the site is not the same
		# Time to alert some good looking people !!!
		alert.alert_people("We have a strange hash ")




def scan_site(site):
	'''
	Here we are scanning a site one by one
	'''

	r  = requests.get(site)
	data = r.text
	soup = BeautifulSoup(data,'html.parser')
	
	
	alert.print_message("Check running on "+site)
	
	for link in soup.find_all('script'):
	    
	    if str(link.get('src')) != "None":
			if str(link.get('src')).startswith('http'):
				hash_file(link.get('src'),site)
			elif str(link.get('src')).startswith('//'):
				hash_file(link.get('src').replace('//','https://'),site)
			else:
				hash_file(site+link.get('src'),site)
			




#Getitng the sites we want to scan and how often
sites = os.environ['sites']
sleep_time = int(os.environ['sleep'])
site_list = sites.split(",")

while True:
	for site in site_list:
		print(site)
		scan_site("https://"+site)
	
	#Sleep for the fime we set before
	time.sleep(sleep_time)





