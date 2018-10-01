from pymongo import MongoClient
import datetime
import hashcache
import alert

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
		alert.print_message("Added a new page "+page_id)
		#And add it to the cache so we dont need to ask here every time !
		hashcache.add_to_redis(id,hash)

		#Return false we did not have this file in db before
		return False

	else:
		#We already has that fil in the db so lets add it to the cache
		alert.print_message("we hade the value in db so add to redis as well")
		hashcache.add_to_redis(id,hash)

		#Return the hash from the db
		return is_there_page["hash"]


