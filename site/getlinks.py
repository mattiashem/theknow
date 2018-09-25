from bs4 import BeautifulSoup
import re
import requests
import hashlib

def hash_file(url):
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
	print("File="+url+" Hash="+hasher.hexdigest())




site = "https://www.alamo.co.uk"
r  = requests.get(site)
data = r.text
soup = BeautifulSoup(data,'html.parser')


print ("Check running on "+site)

for link in soup.find_all('script'):
    
    if str(link.get('src')) != "None":
		if str(link.get('src')).startswith('http'):
			hash_file(link.get('src'))
		elif str(link.get('src')).startswith('//'):
			hash_file(link.get('src').replace('//','https://'))
		else:
			hash_file(site+link.get('src'))
			






