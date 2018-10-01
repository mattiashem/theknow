from pymongo import MongoClient
import datetime

#
# Used to connect to the db 
#
#


## Conenct to mongo and set collection
client = MongoClient('mongo', 27017)
db=client.theknow


def add_file_db(url,id,hash):
	'''
	Adding the file to the db
	'''
	is_there_page = db.pages.find_one({"id":id})

	if is_there_page == "None":
		#We dont have file with that id in the db lets add it !!
		page = {"url": url,
			"id": id,
        	"hash": hash,
         	"version": "latest",
         	"date": datetime.datetime.utcnow()}
		page_id = db.pages.insert_one(page).inserted_id
		print("Added a new page "+page_id)
	else:
		#We already has that fil in the db lest check hash
		print("check hash "+is_there_page["hash"])
		if hash == is_there_page["hash"]:
			# We have the same hash on the site as in our db
			# So we are good :-)
			print("All fine the hash matched") 
		else:
			# Well now we have a problem the hash in the db and from the site is not the same
			# Time to alert some good looking people !!!
			print("ALERT ALERT !!")